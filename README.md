# Historias de Usuario

## Historia 1: Registro de usuario
**Descripción**:  
Como usuario, quiero ingresar mi nombre y correo en el formulario, para registrarme correctamente en la página.

### Criterios de Aceptación:
1. El formulario debe aceptar un nombre de al menos 2 caracteres.
2. El formulario debe aceptar un correo con formato válido (e.g., `usuario@ejemplo.com`).
3. Al presionar "Enviar", debe mostrarse un mensaje de éxito.

### Criterios de Rechazo:
1. Si algún campo está vacío, el formulario debe mostrar un mensaje de error.
2. Si el correo tiene un formato inválido, el formulario no debe enviarse.

---

## Historia 2: Validación de campos vacíos
**Descripción**:  
Como usuario, quiero recibir un mensaje de error si dejo un campo vacío, para saber qué información debo completar.

### Criterios de Aceptación:
1. Si el nombre está vacío, debe aparecer un mensaje: "El campo Nombre es obligatorio."
2. Si el correo está vacío, debe aparecer un mensaje: "El campo Correo es obligatorio."
3. El botón "Enviar" debe estar deshabilitado hasta que se completen todos los campos.

### Criterios de Rechazo:
1. El formulario no debe enviarse si hay campos vacíos.
2. No deben mostrarse mensajes de error incorrectos si todos los campos están llenos.

---

## Historia 3: Validación de formato de correo
**Descripción**:  
Como usuario, quiero recibir un mensaje de error si el correo no tiene un formato válido, para corregirlo antes de enviar.

### Criterios de Aceptación:
1. Si el correo no contiene un "@" o un dominio (e.g., `.com`, `.net`), debe aparecer el mensaje: "Ingrese un correo válido."
2. El formulario no debe enviarse si el correo es inválido.

### Criterios de Rechazo:
1. No deben aceptarse correos incompletos (e.g., `usuario@`, `@ejemplo.com`).
2. No deben aparecer mensajes de error para correos válidos.

---

## Historia 4: Confirmación del registro
**Descripción**:  
Como usuario, quiero recibir una confirmación visual después de enviar el formulario, para asegurarme de que el registro se completó correctamente.

### Criterios de Aceptación:
1. Después de enviar el formulario correctamente, debe mostrarse un mensaje: "Registro exitoso."
2. El formulario debe limpiarse automáticamente después de enviarlo.

### Criterios de Rechazo:
1. No debe mostrarse el mensaje de éxito si hay errores en el formulario.
2. El formulario no debe enviarse más de una vez si se hace clic repetidamente en el botón.

---

## Historia 5: Guardar datos en localStorage
**Descripción**:  
Como usuario, quiero que mis datos ingresados en el formulario se guarden temporalmente en el navegador, para no perder la información si actualizo la página.

### Criterios de Aceptación:
1. Los campos "Nombre" y "Correo" deben rellenarse automáticamente con los últimos valores ingresados si la página se recarga.
2. La información debe guardarse solo en el navegador y no en un servidor externo.

### Criterios de Rechazo:
1. Los datos no deben guardarse si el formulario contiene errores o no se ha completado correctamente.
2. No debe guardarse información confidencial adicional que no sea el nombre y el correo.
