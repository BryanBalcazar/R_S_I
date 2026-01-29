🚀 Guía de Despliegue: Proyecto RSI (Odoo ISP)
Sigue estos pasos en orden para levantar el proyecto con toda la configuración, logos, planes y roles de usuario.

1. Preparación
Asegúrate de tener instalado Docker y Docker Desktop abierto. Descomprime la carpeta del proyecto y abre una terminal dentro de ella.

2. Levantar el Servidor
Este comando descarga las imágenes necesarias y enciende los motores de Odoo y la Base de Datos.

Bash
docker-compose up -d
Espera unos 10 segundos a que los servicios se estabilicen.

3. Cargar la Base de Datos (Backup de 51MB)
Este es el paso clave para que te aparezca todo lo que yo hice (Logo de RSI, planes, eCommerce y roles).

Bash
docker exec -i proyecto_odoo_isp_db_1 psql -U odoo -d postgres < backup_rsi.sql
Nota: Si la terminal vuelve a la línea de comandos sin errores, la carga fue exitosa.

4. Reiniciar para Aplicar Cambios
Reiniciamos los contenedores para que Odoo reconozca la nueva base de datos inyectada.

Bash
docker-compose restart
5. Acceso al Sistema
Abre tu navegador y entra a la siguiente dirección:

URL: http://localhost:8069

Base de Datos: Selecciona postgres (si te lo pregunta).

Credenciales: Usa mi correo y mi contraseña (los mismos que usamos en el laboratorio).