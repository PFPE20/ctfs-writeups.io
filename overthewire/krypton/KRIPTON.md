[*← Back to index*](../../README.md)

# Kripton

* **Dificultad**: Fácil
* **Tipo de reto**: Criptography (Criptografía)

**NOTAS**:
- Cualquier revelación de contraseña ha sido cambiada por **PASSWORD**
- Todos los retos se encuentran en la ruta `/krypton` en el directorio principal.

## Lvl 1 → 2

Este reto es el cifrado conocido **ROT13** el cual podemos hacer en la terminal sin complicaciones.

Comandos: `cat`, `tr`

Iniciamos con una contraseña codificada en base64:

`S1JZUFRPTklTR1JFQVQ=`

Decodificamos y entramos.
```
krypton1@krypton:/krypton/krypton1$ cat README 
Welcome to Krypton!

This game is intended to give hands on experience with cryptography
and cryptanalysis.  The levels progress from classic ciphers, to modern,
easy to harder.

Although there are excellent public tools, like cryptool,to perform
the simple analysis, we strongly encourage you to try and do these
without them for now.  We will use them in later excercises.

** Please try these levels without cryptool first **


The first level is easy.  The password for level 2 is in the file 
'krypton2'.  It is 'encrypted' using a simple rotation called ROT13.  
It is also in non-standard ciphertext format.  When using alpha characters for
cipher text it is normal to group the letters into 5 letter clusters, 
regardless of word boundaries.  This helps obfuscate any patterns.

This file has kept the plain text word boundaries and carried them to
the cipher text.

Enjoy!

krypton1@krypton:/krypton/krypton1$ cat krypton2 | tr 'A-Z' 'N-ZA-M'
PASSWORD
```

---

## Lvl 2 → 3

Este reto consiste en el cifrado **Caesar Cypher**. Hay una herramienta muy buena que lo descifra: https://www.dcode.fr/caesar-cipher

Comandos: `cat`, `xargs`

```
krypton2@krypton:/krypton/krypton2$ ls -la
total 36
drwxr-xr-x 2 root     root      4096 Apr  3 15:18 .
drwxr-xr-x 9 root     root      4096 Apr  3 15:18 ..
-rwsr-x--- 1 krypton3 krypton2 16336 Apr  3 15:18 encrypt
-rw-r----- 1 krypton3 krypton3    27 Apr  3 15:18 keyfile.dat
-rw-r----- 1 krypton2 krypton2    13 Apr  3 15:18 krypton3
-rw-r----- 1 krypton2 krypton2  1815 Apr  3 15:18 README


krypton2@krypton:/krypton/krypton2$ cat README
Krypton 2
...

krypton2@krypton:/krypton/krypton2$ mktemp -d
/tmp/tmp.muFTdnA9Ep
krypton2@krypton:/krypton/krypton2$ cd /tmp/tmp.muFTdnA9Ep
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ ln -s /krypton/krypton2/keyfile.dat .
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ chmod 777 .
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ echo "AABBCCDD" > test.txt
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ /krypton/krypton2/encrypt test.txt 
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ ls
ciphertext  keyfile.dat  test.txt
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ cat ciphertext | xargs
MMNNOOPP
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ /krypton/krypton2/encrypt /krypton/krypton2/krypton3
krypton2@krypton:/tmp/tmp.muFTdnA9Ep$ cat ciphertext | xargs
AYCQYPGQCYQW
```

En este punto pueden ir a: https://www.dcode.fr/caesar-cipher y allí podran descifrar la contraseña.

---

## Lvl 3 → 4

Este reto consiste en "análisis de frecuencia" (*frequency analysis*).

Comandos: `cat`, `tr`, `sort`, `uniq`, `fold`

```
krypton3@krypton:/krypton/krypton3$ cat README 
Well done.  You've moved past an easy substitution cipher.
...

krypton3@krypton:/krypton/krypton3$ cat HINT1
Some letters are more prevalent in English than others.
krypton3@krypton:/krypton/krypton3$ cat HINT2
"Frequency Analysis" is your friend.
krypton3@krypton:/krypton/krypton3$ cat krypton4 
KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
CGZNL YJBEN QYDLQ ZQSUQ NZCYD SNQVU BFGBK GQUQZ QSUQN UZCYD SNJDS UDCXJ ZCYDS NZQSU QNUZB WSBNZ QSUQN UDCXJ CUBGS BXJDS UCTYV SUJQG WTBUJ KCWSV LFGBK GSGZN LYJCB GJSZD GCHMS UCJCU QJLYS BXUMA UJCJM JCBGZ CYDSN CGKDC ZDSQZ DVSJJ SNCGJ DSYVQ CGJSO JCUNS YVQZS WALQV SJJSN UBTSX COSWG MTASN BXYBU CJCBG UWBKG JDSQV YDQAS JXBNS OQTYV SKCJD QUDCX JBXQK BMVWA SNSYV QZSWA LWAKB MVWAS ZBTSS QGWUB BGJDS TSJDB WCUGQ TSWQX JSNRM VCMUZ QSUQN KDBMU SWCJJ BZBTT MGCZQ JSKCJ DDCUE SGSNQ VUJDS SGZNL YJCBG UJSYY SNXBN TSWAL QZQSU QNZCY DSNCU BXJSG CGZBN YBNQJ SWQUY QNJBX TBNSZ BTYVS OUZDS TSUUM ZDQUJ DSICE SGNSZ CYDSN QGWUJ CVVDQ UTBWS NGQYY VCZQJ CBGCG JDSNB JULUJ STQUK CJDQV VUCGE VSQVY DQASJ UMAUJ CJMJC BGZCY DSNUJ DSZQS UQNZC YDSNC USQUC VLANB FSGQG WCGYN QZJCZ SBXXS NUSUU SGJCQ VVLGB ZBTTM GCZQJ CBGUS ZMNCJ LUDQF SUYSQ NSYNB WMZSW TBUJB XDCUF GBKGK BNFAS JKSSG QGWDC USQNV LYVQL UKSNS TQCGV LZBTS WCSUQ GWDCU JBNCS UESGN SUDSN QCUSW JBJDS YSQFB XUBYD CUJCZ QJCBG QGWQN JCUJN LALJD SSGWB XJDSU COJSS GJDZS GJMNL GSOJD SKNBJ STQCG VLJNQ ESWCS UMGJC VQABM JCGZV MWCGE DQTVS JFCGE VSQNQ GWTQZ ASJDZ BGUCW SNSWU BTSBX JDSXC GSUJS OQTYV SUCGJ DSSGE VCUDV QGEMQ ESCGD CUVQU JYDQU SDSKN BJSJN QECZB TSWCS UQVUB FGBKG QUNBT QGZSU QGWZB VVQAB NQJSW KCJDB JDSNY VQLKN CEDJU TQGLB XDCUY VQLUK SNSYM AVCUD SWCGS WCJCB GUBXI QNLCG EHMQV CJLQG WQZZM NQZLW MNCGE DCUVC XSJCT SQGWC GJKBB XDCUX BNTSN JDSQJ NCZQV ZBVVS QEMSU YMAVC UDSWJ DSXCN UJXBV CBQZB VVSZJ SWSWC JCBGB XDCUW NQTQJ CZKBN FUJDQ JCGZV MWSWQ VVAMJ JKBBX JDSYV QLUGB KNSZB EGCUS WQUUD QFSUY SQNSU
krypton3@krypton:/krypton/krypton3$ cat found2
QVJDB MEDGB QJJSG WQGZS NSZBN WUXBN JDSYS NCBWU MNICI STBUJ ACBEN QYDSN UQENS SJDQJ UDQFS UYSQN SKQUS WMZQJ SWQJJ DSFCG EUGSK UZDBB VCGUJ NQJXB NWQXN SSUZD BBVZD QNJSN SWCGQ ABMJQ HMQNJ SNBXQ TCVSX NBTDC UDBTS ENQTT QNUZD BBVUI QNCSW CGHMQ VCJLW MNCGE JDSSV CPQAS JDQGS NQAMJ JDSZM NNCZM VMTKQ UWCZJ QJSWA LVQKJ DNBME DBMJS GEVQG WQGWJ DSUZD BBVKB MVWDQ ISYNB ICWSW QGCGJ SGUCI SSWMZ QJCBG CGVQJ CGENQ TTQNQ GWJDS ZVQUU CZUQJ JDSQE SBXUD QFSUY SQNST QNNCS WJDSL SQNBV WQGGS DQJDQ KQLJD SZBGU CUJBN LZBMN JBXJD SWCBZ SUSBX KBNZS UJSNC UUMSW QTQNN CQESV CZSGZ SBGGB ISTAS NJKBB XDQJD QKQLU GSCED ABMNU YBUJS WABGW UJDSG SOJWQ LQUUM NSJLJ DQJJD SNSKS NSGBC TYSWC TSGJU JBJDS TQNNC QESJD SZBMY VSTQL DQISQ NNQGE SWJDS ZSNST BGLCG UBTSD QUJSU CGZSJ DSKBN ZSUJS NZDQG ZSVVB NQVVB KSWJD STQNN CQESA QGGUJ BASNS QWBGZ SCGUJ SQWBX JDSMU MQVJD NSSJC TSUQG GSUYN SEGQG ZLZBM VWDQI SASSG JDSNS QUBGX BNJDC UUCOT BGJDU QXJSN JDSTQ NNCQE SUDSE QISAC NJDJB QWQME DJSNU MUQGG QKDBK QUAQY JCUSW BGTQL JKCGU UBGDQ TGSJQ GWWQM EDJSN RMWCJ DXBVV BKSWQ VTBUJ JKBLS QNUVQ JSNQG WKSNS AQYJC USWBG XSANM QNLDQ TGSJW CSWBX MGFGB KGZQM USUQJ JDSQE SBXQG WKQUA MNCSW BGQME MUJQX JSNJD SACNJ DBXJD SJKCG UJDSN SQNSX SKDCU JBNCZ QVJNQ ZSUBX UDQFS UYSQN SMGJC VDSCU TSGJC BGSWQ UYQNJ BXJDS VBGWB GJDSQ JNSUZ SGSCG ASZQM USBXJ DCUEQ YUZDB VQNUN SXSNJ BJDSL SQNUA SJKSS GQGWQ UUDQF SUYSQ NSUVB UJLSQ NUACB ENQYD SNUQJ JSTYJ CGEJB QZZBM GJXBN JDCUY SNCBW DQISN SYBNJ SWTQG LQYBZ NLYDQ VUJBN CSUGC ZDBVQ UNBKS UDQFS UYSQN SUXCN UJACB ENQYD SNNSZ BMGJS WQUJN QJXBN WVSES GWJDQ JUDQF SUYSQ NSXVS WJDSJ BKGXB NVBGW BGJBS UZQYS YNBUS ZMJCB GXBNW SSNYB QZDCG EQGBJ DSNSC EDJSS GJDZS GJMNL UJBNL DQUUD QFSUY SQNSU JQNJC GEDCU JDSQJ NCZQV ZQNSS NTCGW CGEJD SDBNU SUBXJ DSQJN SYQJN BGUCG VBGWB GRBDG QMANS LNSYB NJSWJ DQJUD QFSUY SQNSD QWASS GQZBM GJNLU ZDBBV TQUJS NUBTS JKSGJ CSJDZ SGJMN LUZDB VQNUD QISUM EESUJ SWJDQ JUDQF SUYSQ NSTQL DQISA SSGST YVBLS WQUQU ZDBBV TQUJS NALQV SOQGW SNDBE DJBGB XVQGZ QUDCN SQZQJ DBVCZ VQGWB KGSNK DBGQT SWQZS NJQCG KCVVC QTUDQ FSUDQ XJSCG DCUKC VVGBS ICWSG ZSUMA UJQGJ CQJSU UMZDU JBNCS UBJDS NJDQG DSQNU QLZBV VSZJS WQXJS NDCUW SQJD
krypton3@krypton:/krypton/krypton3$ cat found3
DSNSM YBGVS ENQGW QNBUS KCJDQ ENQIS QGWUJ QJSVL QCNQG WANBM EDJTS JDSAS SJVSX NBTQE VQUUZ QUSCG KDCZD CJKQU SGZVB USWCJ KQUQA SQMJC XMVUZ QNQAQ SMUQG WQJJD QJJCT SMGFG BKGJB GQJMN QVCUJ UBXZB MNUSQ ENSQJ YNCPS CGQUZ CSGJC XCZYB CGJBX ICSKJ DSNSK SNSJK BNBMG WAVQZ FUYBJ UGSQN BGSSO JNSTC JLBXJ DSAQZ FQGWQ VBGEB GSGSQ NJDSB JDSNJ DSUZQ VSUKS NSSOZ SSWCG EVLDQ NWQGW EVBUU LKCJD QVVJD SQYYS QNQGZ SBXAM NGCUD SWEBV WJDSK SCEDJ BXJDS CGUSZ JKQUI SNLNS TQNFQ AVSQG WJQFC GEQVV JDCGE UCGJB ZBGUC WSNQJ CBGCZ BMVWD QNWVL AVQTS RMYCJ SNXBN DCUBY CGCBG NSUYS ZJCGE CJ
krypton3@krypton:/krypton/krypton3$ cat found*
CGZNL YJBEN QYDLQ ZQSUQ NZCYD SNQVU BFGBK GQUQZ QSUQN UZCYD SNJDS UDCXJ ZCYDS NZQSU QNUZB WSBNZ QSUQN UDCXJ CUBGS BXJDS UCTYV SUJQG WTBUJ KCWSV LFGBK GSGZN LYJCB GJSZD GCHMS UCJCU QJLYS BXUMA UJCJM JCBGZ CYDSN CGKDC ZDSQZ DVSJJ SNCGJ DSYVQ CGJSO JCUNS YVQZS WALQV SJJSN UBTSX COSWG MTASN BXYBU CJCBG UWBKG JDSQV YDQAS JXBNS OQTYV SKCJD QUDCX JBXQK BMVWA SNSYV QZSWA LWAKB MVWAS ZBTSS QGWUB BGJDS TSJDB WCUGQ TSWQX JSNRM VCMUZ QSUQN KDBMU SWCJJ BZBTT MGCZQ JSKCJ DDCUE SGSNQ VUJDS SGZNL YJCBG UJSYY SNXBN TSWAL QZQSU QNZCY DSNCU BXJSG CGZBN YBNQJ SWQUY QNJBX TBNSZ BTYVS OUZDS TSUUM ZDQUJ DSICE SGNSZ CYDSN QGWUJ CVVDQ UTBWS NGQYY VCZQJ CBGCG JDSNB JULUJ STQUK CJDQV VUCGE VSQVY DQASJ UMAUJ CJMJC BGZCY DSNUJ DSZQS UQNZC YDSNC USQUC VLANB FSGQG WCGYN QZJCZ SBXXS NUSUU SGJCQ VVLGB ZBTTM GCZQJ CBGUS ZMNCJ LUDQF SUYSQ NSYNB WMZSW TBUJB XDCUF GBKGK BNFAS JKSSG QGWDC USQNV LYVQL UKSNS TQCGV LZBTS WCSUQ GWDCU JBNCS UESGN SUDSN QCUSW JBJDS YSQFB XUBYD CUJCZ QJCBG QGWQN JCUJN LALJD SSGWB XJDSU COJSS GJDZS GJMNL GSOJD SKNBJ STQCG VLJNQ ESWCS UMGJC VQABM JCGZV MWCGE DQTVS JFCGE VSQNQ GWTQZ ASJDZ BGUCW SNSWU BTSBX JDSXC GSUJS OQTYV SUCGJ DSSGE VCUDV QGEMQ ESCGD CUVQU JYDQU SDSKN BJSJN QECZB TSWCS UQVUB FGBKG QUNBT QGZSU QGWZB VVQAB NQJSW KCJDB JDSNY VQLKN CEDJU TQGLB XDCUY VQLUK SNSYM AVCUD SWCGS WCJCB GUBXI QNLCG EHMQV CJLQG WQZZM NQZLW MNCGE DCUVC XSJCT SQGWC GJKBB XDCUX BNTSN JDSQJ NCZQV ZBVVS QEMSU YMAVC UDSWJ DSXCN UJXBV CBQZB VVSZJ SWSWC JCBGB XDCUW NQTQJ CZKBN FUJDQ JCGZV MWSWQ VVAMJ JKBBX JDSYV QLUGB KNSZB EGCUS WQUUD QFSUY SQNSU QVJDB MEDGB QJJSG WQGZS NSZBN WUXBN JDSYS NCBWU MNICI STBUJ ACBEN QYDSN UQENS SJDQJ UDQFS UYSQN SKQUS WMZQJ SWQJJ DSFCG EUGSK UZDBB VCGUJ NQJXB NWQXN SSUZD BBVZD QNJSN SWCGQ ABMJQ HMQNJ SNBXQ TCVSX NBTDC UDBTS ENQTT QNUZD BBVUI QNCSW CGHMQ VCJLW MNCGE JDSSV CPQAS JDQGS NQAMJ JDSZM NNCZM VMTKQ UWCZJ QJSWA LVQKJ DNBME DBMJS GEVQG WQGWJ DSUZD BBVKB MVWDQ ISYNB ICWSW QGCGJ SGUCI SSWMZ QJCBG CGVQJ CGENQ TTQNQ GWJDS ZVQUU CZUQJ JDSQE SBXUD QFSUY SQNST QNNCS WJDSL SQNBV WQGGS DQJDQ KQLJD SZBGU CUJBN LZBMN JBXJD SWCBZ SUSBX KBNZS UJSNC UUMSW QTQNN CQESV CZSGZ SBGGB ISTAS NJKBB XDQJD QKQLU GSCED ABMNU YBUJS WABGW UJDSG SOJWQ LQUUM NSJLJ DQJJD SNSKS NSGBC TYSWC TSGJU JBJDS TQNNC QESJD SZBMY VSTQL DQISQ NNQGE SWJDS ZSNST BGLCG UBTSD QUJSU CGZSJ DSKBN ZSUJS NZDQG ZSVVB NQVVB KSWJD STQNN CQESA QGGUJ BASNS QWBGZ SCGUJ SQWBX JDSMU MQVJD NSSJC TSUQG GSUYN SEGQG ZLZBM VWDQI SASSG JDSNS QUBGX BNJDC UUCOT BGJDU QXJSN JDSTQ NNCQE SUDSE QISAC NJDJB QWQME DJSNU MUQGG QKDBK QUAQY JCUSW BGTQL JKCGU UBGDQ TGSJQ GWWQM EDJSN RMWCJ DXBVV BKSWQ VTBUJ JKBLS QNUVQ JSNQG WKSNS AQYJC USWBG XSANM QNLDQ TGSJW CSWBX MGFGB KGZQM USUQJ JDSQE SBXQG WKQUA MNCSW BGQME MUJQX JSNJD SACNJ DBXJD SJKCG UJDSN SQNSX SKDCU JBNCZ QVJNQ ZSUBX UDQFS UYSQN SMGJC VDSCU TSGJC BGSWQ UYQNJ BXJDS VBGWB GJDSQ JNSUZ SGSCG ASZQM USBXJ DCUEQ YUZDB VQNUN SXSNJ BJDSL SQNUA SJKSS GQGWQ UUDQF SUYSQ NSUVB UJLSQ NUACB ENQYD SNUQJ JSTYJ CGEJB QZZBM GJXBN JDCUY SNCBW DQISN SYBNJ SWTQG LQYBZ NLYDQ VUJBN CSUGC ZDBVQ UNBKS UDQFS UYSQN SUXCN UJACB ENQYD SNNSZ BMGJS WQUJN QJXBN WVSES GWJDQ JUDQF SUYSQ NSXVS WJDSJ BKGXB NVBGW BGJBS UZQYS YNBUS ZMJCB GXBNW SSNYB QZDCG EQGBJ DSNSC EDJSS GJDZS GJMNL UJBNL DQUUD QFSUY SQNSU JQNJC GEDCU JDSQJ NCZQV ZQNSS NTCGW CGEJD SDBNU SUBXJ DSQJN SYQJN BGUCG VBGWB GRBDG QMANS LNSYB NJSWJ DQJUD QFSUY SQNSD QWASS GQZBM GJNLU ZDBBV TQUJS NUBTS JKSGJ CSJDZ SGJMN LUZDB VQNUD QISUM EESUJ SWJDQ JUDQF SUYSQ NSTQL DQISA SSGST YVBLS WQUQU ZDBBV TQUJS NALQV SOQGW SNDBE DJBGB XVQGZ QUDCN SQZQJ DBVCZ VQGWB KGSNK DBGQT SWQZS NJQCG KCVVC QTUDQ FSUDQ XJSCG DCUKC VVGBS ICWSG ZSUMA UJQGJ CQJSU UMZDU JBNCS UBJDS NJDQG DSQNU QLZBV VSZJS WQXJS NDCUW SQJDDSNSM YBGVS ENQGW QNBUS KCJDQ ENQIS QGWUJ QJSVL QCNQG WANBM EDJTS JDSAS SJVSX NBTQE VQUUZ QUSCG KDCZD CJKQU SGZVB USWCJ KQUQA SQMJC XMVUZ QNQAQ SMUQG WQJJD QJJCT SMGFG BKGJB GQJMN QVCUJ UBXZB MNUSQ ENSQJ YNCPS CGQUZ CSGJC XCZYB CGJBX ICSKJ DSNSK SNSJK BNBMG WAVQZ FUYBJ UGSQN BGSSO JNSTC JLBXJ DSAQZ FQGWQ VBGEB GSGSQ NJDSB JDSNJ DSUZQ VSUKS NSSOZ SSWCG EVLDQ NWQGW EVBUU LKCJD QVVJD SQYYS QNQGZ SBXAM NGCUD SWEBV WJDSK SCEDJ BXJDS CGUSZ JKQUI SNLNS TQNFQ AVSQG WJQFC GEQVV JDCGE UCGJB ZBGUC WSNQJ CBGCZ BMVWD QNWVL AVQTS RMYCJ SNXBN DCUBY CGCBG NSUYS ZJCGE CJ
```

Entonces podemos ir a https://www.dcode.fr/frequency-analysis para ver la frecuencia de cada letra, habiéndolo encontrado podemos comparar pero no va a representar nada en sí mismo. Sólo tendríamos el conocimiento de cuál es la frecuencia de cada una. O tambíen pueden usar el comando:

`cat found * | tr -cd 'a-zA-Z' | fold -w1 | sort | uniq -c | sort -rn`

Con esta herramienta https://www.boxentriq.com/analysis/frequency-analysis?ref=learnhacking.io podemos calcular la frecuencia y la comparación por cada 3 letras y obtendremos un resultado interesante en la mayor frecuencia que luego usaremos en https://www.quipqiup.com/ para obtener el resultado final.

---

## Lvl 4 → 5

Este reto consiste en el famoso y complejo **Vigenere Cipher**, dejaré una URL que lo descifra de forma automática, sin embargo debemos considerar el "keylenght" del texto para obtener la respuesta.

Comandos: `cat`, `xargs`

```
krypton4@krypton:/krypton/krypton4$ ls
found1  found2  HINT  krypton5  README
krypton4@krypton:/krypton/krypton4$ cat README 
Good job!
...
krypton4@krypton:/krypton/krypton4$ cat HINT 
Frequency analysis will still work, but you need to analyse it
by "keylength".  Analysis of cipher text at position 1, 7, 13, etc
should reveal the 1st letter of the key, in this case.  Treat this as
6 different mono-alphabetic ciphers...

Persistence and some good guesses are the key!
```

Tenemos una clave de 6 dígitos, podemos encontrarla en: https://www.dcode.fr/vigenere-cipher

```
krypton4@krypton:/krypton/krypton4$ cat krypton5 | xargs
HCIKV RJOX
```

En la página web que dejé anteriormente encontraremos toda la solución, nótese que para la contraseña no debemos considerar el espacio.

---

## Lvl 5 → 6

Usaremos exactamente la misma página que el reto anterior: https://www.dcode.fr/vigenere-cipher ; solamente en este no tendremos la longitud de la "key", sin embargo la herramienta lo encontrará de inmediato, una vez encontrada obtendremos la contraseña.

Comandos: `cat`

```
krypton5@krypton:/krypton/krypton5$ ls -la
total 28
drwxr-xr-x 2 root     root     4096 Apr  3 15:18 .
drwxr-xr-x 9 root     root     4096 Apr  3 15:18 ..
-rw-r----- 1 krypton5 krypton5 1776 Apr  3 15:18 found1
-rw-r----- 1 krypton5 krypton5 1915 Apr  3 15:18 found2
-rw-r----- 1 krypton5 krypton5 2110 Apr  3 15:18 found3
-rw-r----- 1 krypton5 krypton5    7 Apr  3 15:18 krypton6
-rw-r----- 1 krypton5 krypton5  151 Apr  3 15:18 README
krypton5@krypton:/krypton/krypton5$ cat README 
Frequency analysis can break a known key length as well.
...
krypton5@krypton:/krypton/krypton5$ cat found1
SXULW GNXIO WRZJG OFLCM RHEFZ ALGSP DXBLM PWIQT XJGLA RIYRI BLPPC HMXMG CTZDL CLKRU YMYSJ TWUTX ZCMRH EFZAL OTMNL BLULV MCQMG CTZDL CPTBI AVPML NVRJN SSXWT XJGLA RIQPE FUGVP PGRLG OMDKW RSIFK TZYRM QHNXD UOWQT XJGLA RIQAV VTZVP LMAIV ZPHCX FPAVT MLBSD OIFVT PBACS EQKOL BCRSM AMULP SPPYF CXOKH LZXUO GNLID ZVRAL DOACC INREN YMLRH VXXJD XMSIN BXUGI UPVRG ESQSG YKQOK LMXRS IBZAL BAYJM AYAVB XRSIC KKPYH ULWFU YHBPG VIGNX WBIQP RGVXY SSBEL NZLVW IMQMG YGVSW GPWGG NARSP TXVKL PXWGD XRJHU SXQMI VTZYO GCTZR JYVBK MZHBX YVBIT TPVTM OOWSA IERTA SZCOI TXXLY JAZQC GKPCS LZRYE MOOVC HIEKT RSREH MGNTS KVEPN NCTUN EOFIR TPPDL YAPNO GMKGC ZRGNX ARVMY IBLXU QPYYH GNXYO ACCIN QBUQA GELNR TYQIH LANTW HAYCP RJOMO KJYTV SGVLY RRSIG NKVXI MQJEG GJOML MSGNV VERRC MRYBA GEQNP RGKLB XFLRP XRZDE JESGN XSYVB DSSZA LCXYE ICXXZ OVTPW BLEVK ZCDEA JYPCL CDXUG MARML RWVTZ LXIPL PJKKL CIREP RJYVB ITPVV ZPHCX FPCRG KVPSS CPBXW VXIRS SHYTU NWCGI ANNUN VCOEA JLLFI LECSO OLCTG CMGAT SBITP PNZBV XWUPV RIHUM IBPHG UXUQP YYHNZ MOKXD LZBAK LNTCC MBJTZ KXRSM FSKZC SSELP UMARE BCIPK GAVCY EXNOG LNLCC JVBXH XHRHI AZBLD LZWIF YXKLM PELQG RVPAF ZQNVK VZLCE MPVKP FERPM AZALV MDPKH GKKCL YOLRX TSNIB ELRYN IVMKP ECVXH BELNI OETUX SSYGV TZARE RLVEG GNOQC YXFCX YOQYO ISUKA RIQHE YRHDS REFTB LEVXH MYEAJ PLCXK TRFZX YOZCY XUKVV MOJLR RMAVC XFLHO KXUVE GOSAR RHBSS YHQUS LXSDJ INXLH PXCCV NVIPX KMFXV ZLTOW QLKRY TZDLC DTVXB ACSDE LVYOL BCWPE ERTZD TYDXF AILBR YEYEG ESIHC QMPOX UDMLZ VVMBU KPGEC EGIWO HMFXG NXPBW KPVRS XZCEE PWVTM OOIYC XURRV BHCCS SKOLX XQSEQ RTAOP WNSZK MVDLC PRTRB ZRGPZ AAGGK ZIMAP RLKVW EAZRT XXZCS DMVVZ BZRWS MNRIM ZSRYX IEOVH GLGNL FZKHX KCESE KEHDI FLZRV KVFIB XSEKB TZSPE EAZMV DLCSY ZGGYK GCELN TTUIG MXQHT BJKXG ZRFEX ABIAP MIKWA RVMFK UGGFY JRSIP NBJUI LDSSZ ALMSA VPNTX IBSMO
```

---

## Lvl 6 → 7

Para solucionar este reto hay que leer bien las instrucciones en: https://overthewire.org/wargames/krypton/krypton6.html

Una vez entendido lo que hace el binario podemos notar que encripta aleatoriamente los caracteres, sin embargo tiene un patrón de repetición periódico por vueltas. Lo que debemos hacer es contar la diferencia del patrón repetido vs la letra **A** ya que es la primera LETRA en "ASCII", además estamos usando sólo mayúsculas por lo que hace que sea más fácil calcular el "offset" de cada letra, y en caso que NO ESTÉ en **ASCII Mayúsculas** se suma 26 para que se incorpore en el grupo de las mayúsculas, por favor si no sabes lo que es "ASCII" búscalo en internet.

Recomendación para este reto: Si no entiendes muy bien lo que está ocurriendo intenta usar scripts oneliner de python en la terminal y ver el entero ASCII de cada letra:

`python3 -c 'print(ord("A"))'`

Comandos: `cat`, `xargs`, `python3`

```
krypton6@krypton:/krypton/krypton6$ ls -la
total 56
drwxr-xr-x 3 root     root      4096 Apr  3 15:18 .
drwxr-xr-x 9 root     root      4096 Apr  3 15:18 ..
-rwsr-x--- 1 krypton7 krypton6 16528 Apr  3 15:18 encrypt6
-rw-r----- 1 krypton6 krypton6   164 Apr  3 15:18 HINT1
-rw-r----- 1 krypton6 krypton6    11 Apr  3 15:18 HINT2
-rw-r----- 1 krypton7 krypton7    11 Apr  3 15:18 keyfile.dat
-rw-r----- 1 krypton6 krypton6    15 Apr  3 15:18 krypton7
drwxr-xr-x 2 root     root      4096 Apr  3 15:18 onetime
-rw-r----- 1 krypton6 krypton6  4342 Apr  3 15:18 README
krypton6@krypton:/krypton/krypton6$ cat HINT1
The 'random' generator has a limited number of bits, and is periodic.
Entropy analysis and a good look at the bytes in a hex editor will help.

There is a pattern!
krypton6@krypton:/krypton/krypton6$ cat HINT2
8 bit LFSR
krypton6@krypton:/krypton/krypton6$ mktemp -d
/tmp/tmp.XxqgoOGP3a
krypton6@krypton:/krypton/krypton6$ cd /tmp/tmp.XxqgoOGP3a
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ ln -s /krypton/krypton6/keyfile.dat 
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ echo "AAAAA" > test.txt
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ chmod 777 .
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ ls -l
total 4
lrwxrwxrwx 1 krypton6 krypton6 29 May  6 07:38 keyfile.dat -> /krypton/krypton6/keyfile.dat
-rw-rw-r-- 1 krypton6 krypton6  6 May  6 07:38 test.txt
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ cat cipher.txt | xargs
EICTD
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ cat cipher2.txt | xargs
EICTD
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ cat cipher* | xargs
EICTDEICTD
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ python3 -c 'print("A"*50)' > test2.txt
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ /krypton/krypton6/encrypt6 test2.txt /tmp/tmp.XxqgoOGP3a/cipher3.txt
krypton6@krypton:/tmp/tmp.XxqgoOGP3a$ cat cipher3.txt | xargs
EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXY
```

El patrón se repite:
`EICTDGYIYZKTHNSIRFXYCPFUEOCKRN` `EICTDGYIYZKTHNSIRFXY`

En nuestra máquina, vamos a hacer algún script con python para entender que está ocurriendo:

```
❯ touch decipher.py
❯ chmod 777 decipher.py
```

```python
#!/usr/bin/env python3

import string

encrypted_string = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
given = "A" * len(encrypted_string)

to_decipher = "PNUKLYLWRQKGKBE"

positions = list()

# Primero encontremos el offset

for i in range(0, len(encrypted_string)):
    positions.append(ord(encrypted_string[i]) - ord(given[i]))

key = ""

for i in range(0, len(to_decipher)):
    char = ord(to_decipher[i])
    res = char - positions[i]
    if (chr(res) not in string.ascii_letters):
        res = char - positions[i] + 26

    key += chr(res)

print(key)
```

Así obtendremos la contraseña para este último reto. Además dejaré el script original si lo desean usar:

[Python script](./decipher.py)

Hasta aquí llega el write-up de **Krypton**, espero les haya gustado y sea útil para ustedes, para mi fue muy divertido aprender sobre esta parte de la criptografía, un consejo que puedo dejar es utilizar las herramientas que ya se encuentran desarrolladas en internet o paquetes de Linux, softwares de terceros, etc. Si es cierto que aprender "el porqué" de las cosas es importante pero muchas veces esto nos podría conllevar a "reinventar la rueda" lo que toma tiempo extra.

[*← Back to index*](../../README.md)