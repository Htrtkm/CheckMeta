#!/bin/sh

position="ru"

python extractAnnotatedReads.py bov2_${position}_corepfam.out

taxonkit lineage -j 8 --data-dir /data2/takumi/DB/kaijudb_162/ -r taxid.txt | cut -f 1,3 | grep species | grep -v subspecies | cut -f 1 | sort | uniq > taxid_dereplicated.txt

python extractMajorSpecies.py bov2_${position}_corepfam_species.txt > majorSpecies.txt

cat majorSpecies.txt | taxonkit --data-dir /data2/takumi/DB/kaijudb_162/ name2taxid |cut -f 2 > majorSpeciesTaxid.tsv

python makeFastqFiles.py readName_taxid.tsv taxid_dereplicated.txt majorSpeciesTaxid.tsv PE_R1.fastq.trimmed PE_R2.fastq.trimmed

ls | grep PE_R1 > fastqList_R1.txt
ls | grep PE_R2 > fastqList_R2.txt

cat fastqList_R1.txt | while read line; do
	bwa mem -o ${line:6:$((${#line}-32))}.sam -t 20 ${position}_finalseq.fa ./${line} ./${line:0:4}2${line:5:$((${#line}-5))}
	python count_maprate.py ${line} ${line:0:4}2${line:5:$((${#line}-5))} ${line:6:$((${#line}-32))}.sam
done

rm PE_R*
rm *.sam
