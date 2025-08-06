# Curso de Introducción a Git y GitHub

¡Bienvenido al curso de introducción a Git y GitHub! Este repositorio contiene ejercicios prácticos para que aprendas a trabajar con control de versiones y colaboración en proyectos de software.

## Descripción del Proyecto

Este proyecto está diseñado para ayudarte a aprender los conceptos básicos de Git y GitHub mediante la práctica. El archivo principal `main.py` contiene ejercicios intencionalmente erróneos que deberás corregir para aprender a identificar y solucionar problemas en código, mientras practicas los comandos de Git.

## Cómo Ejecutar el Script

Para ejecutar el script y verificar si has corregido los errores correctamente, sigue estos pasos:

1. Abre una terminal en tu computadora
2. Navega al directorio donde clonaste este repositorio
3. Ejecuta el siguiente comando:

```bash
python main.py
```

Inicialmente, el script mostrará mensajes indicando qué ejercicios tienen errores. Tu tarea es corregir estos errores en el código para que todas las pruebas pasen.

## Instrucciones del Ejercicio

1. Clona este repositorio usando el comando:

   ```bash
   git clone https://github.com/TATABOX42/CursoBSG
   ```
2. Crea una nueva rama con tus iniciales usando el comando:

   ```bash
   # Ejemplo, si tus iniciales son BTH, el comando seria
   # git checkout -b feat-BTH
   git checkout -b feat-<tus-iniciales>
   ```
3. Abre el archivo `main.py` en tu Visual Studio Code
4. Corrige los errores en las tres funciones de los ejercicios
5. Valida que el codigo se ejecuta correctamente al ejecutar

   ```bash
   python main.py
   ```

   Si el mensaje en la consola es `Felicidades, todas las pruebas pasaron` , felicidades has corregido los errores y puedes seguir al siguiente paso
6. Guarda tus cambios
7. Añade tus cambios al área de preparación con:

   ```bash
   git add main.py
   ```
8. Realiza un commit con tus cambios:

   ```bash
   git commit -m "feat-bug-fixes"
   ```
9. Sube tus cambios a GitHub (al hacer push de tu rama):

   ```bash
   git push origin feat-<tus-iniciales>
   ```
10. Crea un Pull Request en GitHub para que tus cambios sean revisados

## Explicación de Comandos de Git

### `git clone`

El comando `git clone` se utiliza para crear una copia local de un repositorio remoto.

```bash
git clone <url-del-repositorio>
```

Este comando descarga todo el historial del proyecto y crea una carpeta con el nombre del repositorio.

**Buenas prácticas:**

- Siempre verifica la URL del repositorio antes de clonarlo
- Asegúrate de tener permisos para acceder al repositorio

### `git checkout -b`

El comando `git checkout -b` crea una nueva rama y cambia a ella automáticamente.

```bash
git checkout -b <nombre-de-la-rama>
```

Trabajar con ramas es una práctica fundamental en Git que permite desarrollar nuevas características sin afectar la rama principal.

**Buenas prácticas:**

- Usa nombres descriptivos para las ramas (por ejemplo, `feat-login`, `fix-bug-123`)
- Crea una rama nueva para cada característica o corrección

### `git add`

El comando `git add` añade cambios al área de preparación (staging area).

```bash
git add <nombre-del-archivo>
```

Esto prepara los cambios para ser incluidos en el próximo commit.

**Buenas prácticas:**

- Añade solo los archivos que deseas incluir en el próximo commit
- Usa `git add .` para añadir todos los cambios en el directorio actual (con precaución)

### `git commit`

El comando `git commit` guarda los cambios del área de preparación en el historial del repositorio.

```bash
git commit -m "mensaje descriptivo del cambio"
```

**Buenas prácticas:**

- Escribe mensajes de commit claros y descriptivos
- Usa el imperativo en los mensajes ("Añadir función de login" en lugar de "Añadida función de login")
- Haz commits pequeños y frecuentes en lugar de grandes cambios

### `git push`

El comando `git push` envía los commits locales al repositorio remoto.

```bash
git push origin <nombre-de-la-rama>
```

**Buenas prácticas:**

- Verifica que tus cambios locales estén correctos antes de hacer push
- Asegúrate de estar en la rama correcta antes de hacer push

## Cómo Crear un Pull Request

Un Pull Request (PR) es una solicitud para fusionar tus cambios en la rama principal del proyecto. Para crear un PR:

1. Después de hacer `git push`, ve al repositorio en GitHub
2. Verás un mensaje destacado que dice "Compare & pull request" - haz clic en él
3. Asegúrate de que las ramas base y comparación sean correctas
4. Escribe un título y descripción descriptivos para tu PR
5. Haz clic en "Create pull request"

**Buenas prácticas para PRs:**

- Escribe una descripción clara de qué cambios estás proponiendo
- Referencia cualquier issue relacionado
- Revisa tu código antes de crear el PR
- Sé receptivo a los comentarios de revisión

## Tips y Buenas Prácticas

1. **Antes de comenzar a trabajar:**

   - Asegúrate de tener la última versión del código ejecutando `git pull origin master`
2. **Durante el desarrollo:**

   - Haz commits frecuentes con mensajes descriptivos
   - Mantén tus ramas actualizadas con la rama principal
3. **Antes de crear un PR:**

   - Verifica que tu código funciona correctamente
   - Asegúrate de que no hay errores de sintaxis
4. **Comunicación:**

   - Sé claro en los mensajes de commit y en las descripciones de PR
   - No temas pedir ayuda si encuentras problemas

¡Buena suerte con el ejercicio!
