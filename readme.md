****************************************instalacion parcho grid y BD

        home oracle
/u01/app/oracle/product/19c/db

        home grid
/u01/app/grid/product/19c/crs

**revisar el inventario
$ /u01/app/grid/product/19c/crs/OPatch/opatch lsinventory -detail -oh /u01/app/grid/product/19c/crs

**descomprimir archivo
p34762026_190000_Linux-x86-64.zip
34762026

**revisar errores en parchos
As the Grid home user:

% $ORACLE_HOME/OPatch/opatch prereq CheckConflictAgainstOHWithDetail -phBaseDir /media/34762026/34765931
																				
% $ORACLE_HOME/OPatch/opatch prereq CheckConflictAgainstOHWithDetail -phBaseDir /media/34762026/34768559
																				
% $ORACLE_HOME/OPatch/opatch prereq CheckConflictAgainstOHWithDetail -phBaseDir /media/34762026/34768569
																				
% $ORACLE_HOME/OPatch/opatch prereq CheckConflictAgainstOHWithDetail -phBaseDir /media/34762026/34863894
																				
% $ORACLE_HOME/OPatch/opatch prereq CheckConflictAgainstOHWithDetail -phBaseDir /media/34762026/33575402


**revisar espacio de instalacion
GRID

vi /tmp/patch_list_gihome.txt
/media/34762026/34765931
/media/34762026/34768559
/media/34762026/34768569

$ORACLE_HOME/OPatch/opatch prereq CheckSystemSpace -phBaseFile /tmp/patch_list_gihome.txt

BASE DE DATOS

/media/34762026/34765931
/media/34762026/34768559
ORACLE_HOME/OPatch/opatch prereq CheckSystemSpace -phBaseFile /tmp/patch_list_dbhome.txt


**si es un cluster verificar con este comando con las variable del grid, desde cualquier lado
cluvfy stage -pre patch

***********utilizar el opatch version OPatch 12.2.0.1.37


con root exporta las variables y parchar 
GRID
export ORACLE_SID=+ASM
export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=/u01/app/grid/product/19c/crs
export PATH=/u01/app/grid/product/19c/crs/OPatch:/u01/app/grid/product/19c/crs/bin:/usr/sbin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/s

BD
export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=/u01/app/oracle/product/19c/db
export PATH=/u01/app/oracle/product/19c/db/OPatch:/u01/app/oracle/product/19c/db/bin:/usr/sbin:/usr/lib64/qt-3.3/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/oracle/bin:/u01/app/oracle/product/19c/db/jdk/bin

**nota: subir las BD para el parchado de las BD, para que el proceso corra el script de parchado, 
en dado caso ver mas abajo como correr los script luego del parchado

To patch the Grid home and all Oracle RAC database homes of the same version:
# opatchauto apply /media/34762026

To patch only the Grid home:
# opatchauto apply /media/34762026 -oh /u01/app/grid/product/19c/crs

To patch one or more Oracle RAC database homes:
# opatchauto apply /media/34762026 -oh /u01/app/oracle/product/19c/db

standalone DB
setear las variable de la BD
entrar a la BD
subirla normal
salir
cd $ORACLE_HOME/OPatch
./datapatch -verbose

container DB
setear las variable de la BD
entrar a la BD
subirla normal
alter pluggable database all open;
salir
cd $ORACLE_HOME/OPatch
./datapatch -verbose

cuando se parche la BD correr script objetos invalido

cd $ORACLE_HOME/rdbms/admin
sqlplus / as sysdba
@utlrp.sql


*********parchado de java

setear variable de BD del bash profile en el home de 19c
export PATH=$ORACLE_HOME/perl/bin:$PATH
export PERL5LIB=$ORACLE_HOME/perl/lib

descomprimir archivo
entrar a la ruta del parcho
/media/34786990
correr revision del parcho = opatch prereq CheckConflictAgainstOHWithDetail -ph ./

luego de eso, aplicar parcho 

opatch apply


necesito que me documente este codigo en 