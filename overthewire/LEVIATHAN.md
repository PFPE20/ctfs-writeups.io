
[*← Back to index*](../README.md)

# Leviathan

* **Dificultad**: Fácil
* **Tipo de reto**: Comandos de sistemas operativos basados en *UNIX*

**NOTA**: Cualquier revelación de contraseña ha sido cambiada por **PASSWORD**

## Lvl 0 → 1

Buscando un poco, encontramos en el directorio del usuario (*leviathan0*) un directorio llamado `.backup`, si ingresamos podremos encontrar un archivo `.html`, simplemente se hace un grep para encontrar la palabra **password**, allí aparecerá la contraseña para el siguiente nivel.

Comandos: `grep -i pass`

```bash
leviathan0@leviathan:~$ pwd
/home/leviathan0
leviathan0@leviathan:~$ ls -la
total 24
drwxr-xr-x   3 root       root       4096 Apr  3 15:19 .
drwxr-xr-x 150 root       root       4096 Apr  3 15:20 ..
drwxr-x---   2 leviathan1 leviathan0 4096 Apr  3 15:19 .backup
-rw-r--r--   1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root       3851 Apr  3 15:10 .bashrc
-rw-r--r--   1 root       root        807 Mar 31  2024 .profile
leviathan0@leviathan:~$ cat /etc/leviathan_pass/leviathan1
cat: /etc/leviathan_pass/leviathan1: Permission denied
leviathan0@leviathan:~$ cd .backup/
leviathan0@leviathan:~/.backup$
leviathan0@leviathan:~/.backup$ ls -la
total 140
drwxr-x--- 2 leviathan1 leviathan0   4096 Apr  3 15:19 .
drwxr-xr-x 3 root       root         4096 Apr  3 15:19 ..
-rw-r----- 1 leviathan1 leviathan0 133259 Apr  3 15:19 bookmarks.html
cat bookmarks.html | grep -i pass
<DT><A HREF="http://www.goshen.edu/art/ed/teachem.htm" ADD_DATE="1146092098" LAST_CHARSET="ISO-8859-1" ID="98012771">Pass it
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PASSWORD" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

---

## Lvl 1 → 2

En el directorio del usuario encontraremos un binario el cuál nos pedirá un *string*, ese string lo almacena y luego lo compara usando la función `strcmp` (string compare).

Comandos:

- `ltrace ./binario`
- `file binario` → Yo suelo usar este comando para saber si estoy lidiando con un binario compilado dinámicamente o estáticamente, de esa forma sabré si debo alternar entre *ltrace*, *strace* o si directamente debo usar *gdb*

```bash
leviathan1@leviathan:~$ pwd
/home/leviathan1
leviathan1@leviathan:~$ ls -la
total 36
drwxr-xr-x   2 root       root        4096 Apr  3 15:19 .
drwxr-xr-x 150 root       root        4096 Apr  3 15:20 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Apr  3 15:10 .bashrc
-r-sr-x---   1 leviathan2 leviathan1 15088 Apr  3 15:19 check
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan1@leviathan:~$ file check
check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=5222b367f5b1ff23a8b2d18696bf508c8c8c0e82, for GNU/Linux 3.2.0, not stripped
leviathan1@leviathan:~$ ./check
password: test
Wrong password, Good Bye ...
leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(0x80490ed, 1, 0xffffd474, 0 <unfinished ...>
printf("password: ")                                                                                                 = 10
getchar(0, 0, 0x786573, 0x646f67password: test
)                                                                                    = 116
getchar(0, 116, 0x786573, 0x646f67)                                                                                  = 101
getchar(0, 0x6574, 0x786573, 0x646f67)                                                                               = 115
strcmp("test", "PASSWORD")                                                                                                 = 1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                                                 = 29
+++ exited (status 0) +++
leviathan1@leviathan:~$ ./check
password: PASSWORD
$ whoami
leviathan2
$ cat /etc/leviathan_pass/leviathan2
PASSWORD
```

---

## Lvl 2 → 3

En este reto encontraremos un binario que imprime el contenido de los archivos que le pasemos, intenté usarlo directamente sobre el archivo que contiene la contraseña pero no funcionó. Después de probar con `.bash_logout` pude notar que era por los permisos, aquí pude entender que debido a esto mismo no iba a poder ejecutar `cp` porque los mismos permisos no me lo permitirían. Creamos un directorio temporal y nos dirijimos a él, allí creamos un archivo que contenga *2 palabras* yo lo he llamado "my file.txt", asignamos permisos abiertos para todos los usuarios de forma recursiva al directorio temporal y creamos un link "simbólico" que apunte hacia **la primera palabra** del archivo que creamos, posteriormente la contraseña se almacenará en nuestro archivo.

**¿Qué ocurrió?**

Esta es una vulnerabilidad conocida llamada "TOCTOU" (Time Of check Time Of Use) y se encuentra en la función `access()` y `system()` (en este caso), lo que ocurre es que `access()` comprueba que el archivo (my file.txt) reciba el path del archivo como un string y perteneza al usuario, lo trata como un único archivo. Luego el binario ejecuta el comando `/bin/cat /tmp/.../my file.txt` y lo pasa a `system()` que lo ejecutará en otra shell, la vulnerabilidad empieza en que esta shell no sabe que es un mismo archivo, para ella son dos argumentos separados por lo que `cat` intenta leer el syslink que a su vez apunta al archivo real, por lo que terminamos leyendo la contraseña.

Mapa:

```
printfile → corre como leviathan3
    ↓
system() → lanza cat como leviathan3
    ↓
cat recibe *my* como argumento
    ↓
*my* es un syslink → lo sigue
    ↓
/etc/leviathan_pass_/leviathan3 → se lee
    ↓
leviathan3 tiene permisos → PASSWORD
```

Comandos:

- `mktemp -d`
- `ln -s /archivo /ruta`

```bash
leviathan2@leviathan:~$ pwd
/home/leviathan2
leviathan2@leviathan:~$ ls -la
total 36
drwxr-xr-x   2 root       root        4096 Apr  3 15:19 .
drwxr-xr-x 150 root       root        4096 Apr  3 15:20 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Apr  3 15:10 .bashrc
-r-sr-x---   1 leviathan3 leviathan2 15076 Apr  3 15:19 printfile
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan2@leviathan:~$ file printfile 
printfile: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=efe166cf833ba66423e2645c81c3c30c1049439a, for GNU/Linux 3.2.0, not stripped
leviathan2@leviathan:~$ ./printfile 
*** File Printer ***
Usage: ./printfile filename
leviathan2@leviathan:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...
leviathan2@leviathan:~$ ltrace ./printfile .bash_logout 
__libc_start_main(0x80490ed, 2, 0xffffd464, 0 <unfinished ...>
access(".bash_logout", 4)                                                                                            = 0
snprintf("/bin/cat .bash_logout", 511, "/bin/cat %s", ".bash_logout")                                                = 21
geteuid()                                                                                                            = 12002
geteuid()                                                                                                            = 12002
setreuid(12002, 12002)                                                                                               = 0
system("/bin/cat .bash_logout"# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                               = 0
+++ exited (status 0) +++
leviathan2@leviathan:~$ mktemp -d
/tmp/tmp.KJwGgHsyqO
leviathan2@leviathan:~$ touch /tmp/tmp.KJwGgHsyqO/"my file.txt"
leviathan2@leviathan:~$ ls -la /tmp/tmp.KJwGgHsyqO
total 512
drwx------     2 leviathan2 leviathan2   4096 Apr 25 19:32 .
drwxrwx-wt 11849 root       root       516096 Apr 25 19:32 ..
-rw-rw-r--     1 leviathan2 leviathan2      0 Apr 25 19:32 my file.txt
leviathan2@leviathan:~$ chmod -R 777 /tmp/tmp.KJwGgHsyqO
leviathan2@leviathan:~$ ln -s /etc/leviathan_pass/leviathan3 /tmp/tmp.KJwGgHsyqO/my
leviathan2@leviathan:~$ ls -la /tmp/tmp.KJwGgHsyqO
total 512
drwxrwxrwx     2 leviathan2 leviathan2   4096 Apr 25 19:35 .
drwxrwx-wt 11852 root       root       516096 Apr 25 19:35 ..
lrwxrwxrwx     1 leviathan2 leviathan2     30 Apr 25 19:35 my -> /etc/leviathan_pass/leviathan3
-rwxrwxrwx     1 leviathan2 leviathan2      0 Apr 25 19:32 my file.txt
leviathan2@leviathan:~$ ./printfile /tmp/tmp.KJwGgHsyqO/"my file.txt"
PASSWORD
```



---

## Lvl 3 → 4

En el directorio encontraremos un binario que pide un *string*, si le pasamos una contraseña incorrecta imprime: *bzzzzzzzzap. WRONG*, lo analizamos con `ltrace` y podemos notar que hace dos comparaciones, la primera podría ser una variable de entorno o una variable interna del binario, la segunda es la que compara nuestra *string* con la contraseña, allí podremos obtenerla.

Comandos: `ltrace`

```bash
leviathan3@leviathan:~$ ls -la
total 40
drwxr-xr-x   2 root       root        4096 Apr  3 15:19 .
drwxr-xr-x 150 root       root        4096 Apr  3 15:20 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Apr  3 15:10 .bashrc
-r-sr-x---   1 leviathan4 leviathan3 18100 Apr  3 15:19 level3
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan3@leviathan:~$ ./level3 
Enter the password> test
bzzzzzzzzap. WRONG
ltrace ./level3 
__libc_start_main(0x80490ed, 1, 0xffffd474, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                                                                                           = -1
printf("Enter the password> ")                                                                                       = 20
fgets(Enter the password> test
"test\n", 256, 0xf7fab5c0)                                                                                     = 0xffffd24c
strcmp("test\n", "PASSWORD\n")                                                                                      = 1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                                                                           = 19
+++ exited (status 0) +++
leviathan3@leviathan:~$ ./level3
Enter the password> PASSWORD
[You've got shell]!
$ whoami
leviathan4
$ cat /etc/leviathan_pass/leviathan4
PASSWORD
```

---

## Lvl 4 → 5

En el directorio del usuario (leviathan4) podemos encontrar un directorio oculto llamado **.trash** accedemos a él. Dentro encontramos un binario, al ejecutarlo nos dará un string escrito **representación binaria de una cadena de texto** (*binary encoded-string*), esto lo podemos descifrar usando un script one-line de python, para eso debemos saber si tenemos acceso a `python3` y si lo tenemos ejecutamos el script, en [esta herramienta](https://github.com/PFPE20/find_commands) puedes encontrar varios script oneliner que he indexado a lo largo de la resolución de retos.

Comandos:

- `file`
- `which`
- `python3 -c`

```bash
leviathan4@leviathan:~$ ls -la
total 24
drwxr-xr-x   3 root root       4096 Apr  3 15:19 .
drwxr-xr-x 150 root root       4096 Apr  3 15:20 ..
-rw-r--r--   1 root root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root root       3851 Apr  3 15:10 .bashrc
-rw-r--r--   1 root root        807 Mar 31  2024 .profile
dr-xr-x---   2 root leviathan4 4096 Apr  3 15:19 .trash
leviathan4@leviathan:~$ cd .trash
leviathan4@leviathan:~/.trash$ ls -la
total 24
dr-xr-x--- 2 root       leviathan4  4096 Apr  3 15:19 .
drwxr-xr-x 3 root       root        4096 Apr  3 15:19 ..
-r-sr-x--- 1 leviathan5 leviathan4 14944 Apr  3 15:19 bin
leviathan4@leviathan:~/.trash$ file bin
bin: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=da2bc992d78bb31f01fa19c9fd0e6d02c042a757, for GNU/Linux 3.2.0, not stripped
leviathan4@leviathan:~/.trash$ ./bin
00110000 01100100 01111001 01111000 01010100 00110111 01000110 00110100 01010001 01000100 00001010 
leviathan4@leviathan:~/.trash$ which python3
/usr/bin/python3
leviathan4@leviathan:~/.trash$ ./bin | python3 -c 'import sys; print("".join(chr(int(b,2)) for b in sys.stdin.read().split()))'
PASSWORD
```

---

## Lvl 5 → 6

Encontraremos un binario con los permisos correspondientes para ejecutarlo, el binario intenta leer un archivo llamado `file.log` en el directorio `tmp` (`/tmp/file.log`), intenté crearlo y darle permisos porque no sabía realmente si copiaba allí la información, al no funcionar pasé a hacer un syslink y funcionó.

Comandos:

- `file binario`
- `ltrace`
- `ln -s /archivo /ruta`

```bash
leviathan5@leviathan:~$ ls -la
total 36
drwxr-xr-x   2 root       root        4096 Apr  3 15:19 .
drwxr-xr-x 150 root       root        4096 Apr  3 15:20 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Apr  3 15:10 .bashrc
-r-sr-x---   1 leviathan6 leviathan5 15148 Apr  3 15:19 leviathan5
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan5@leviathan:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@leviathan:~$ ltrace ./leviathan5 
__libc_start_main(0x804910d, 1, 0xffffd464, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                                                          = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)                                                                                    = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan5@leviathan:~$ touch /tmp/file.log
leviathan5@leviathan:~$ chmod 777 /tmp/file.log
chmod: cannot access '/tmp/file.log': No such file or directory
leviathan5@leviathan:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@leviathan:~$ touch /tmp/file.log && chmod 777 /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
leviathan5@leviathan:~$ cat /tmp/file.log
cat: /tmp/file.log: No such file or directory
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
PASSWORD
```


---

## Lvl 6 → 7

En este reto hay un binario que si se ejecuta nos va a pedir un número de 4 digitos, tenemos 9999 alternativas para esto así que simplemente le dejo correr un bucle `for` hasta que encuentre la coincidencia. Nótese que deberían aparecer 9998 **Wrong** pero hay un motivo por el cual no he hecho una bifurcación/bloque if-else en el bucle for, mejor probar cada uno con sus métodos y luego tomar anotaciones.

Comandos:

- `for i in $(TTY); do #lógica; done`
- `whoami`
- `cat`

```bash
leviathan6@leviathan:~$ ls -la
total 36
drwxr-xr-x   2 root       root        4096 Apr  3 15:19 .
drwxr-xr-x 150 root       root        4096 Apr  3 15:20 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Apr  3 15:10 .bashrc
-r-sr-x---   1 leviathan7 leviathan6 15040 Apr  3 15:19 leviathan6
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan6@leviathan:~$ ./leviathan6 
usage: ./leviathan6 <4 digit code>
leviathan6@leviathan:~$ ./leviathan6 1010
Wrong
leviathan6@leviathan:~$ for i in $(seq -w 0 9999); do ./leviathan6 "$i"; done

Lo anterior va a lanzar un montón de "Wrong" en la terminal, hay que esperar que encuentre el número correcto.

...
Wrong
Wrong
Wrong
$ whoami
leviathan7
$ cat /etc/leviathan_pass/leviathan7
PASSWORD
```

Hasta aquí el write-up sobre **leviathan** ya que no hay más retos luego, espero que les guste y les pueda ser útil a aquellos que necesitan ayuda con la resolución del CTF.