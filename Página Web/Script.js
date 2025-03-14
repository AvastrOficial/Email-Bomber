function openSpamMenu() {
            document.getElementById('spamMenu').style.display = 'block';
        }
        function closeSpamMenu() {
            document.getElementById('spamMenu').style.display = 'none';
        }
        function showSection(event, sectionId) {
            event.preventDefault();
            document.querySelectorAll('.section').forEach(section => {
                section.classList.remove('active');
            });
            document.getElementById(sectionId).classList.add('active');
            
            document.querySelectorAll('.nav a').forEach(link => {
                link.classList.remove('active');
            });
            event.target.classList.add('active');
        }
      
        document.getElementById('emailForm').addEventListener('submit', async function(event) {
            event.preventDefault();
            const data = {
                server: document.getElementById('server').value,
                user: document.getElementById('user').value,
                pwd: document.getElementById('pwd').value,
                to: document.getElementById('to').value,
                subject: document.getElementById('subject').value,
                body: document.getElementById('body').value,
                nomes: document.getElementById('nomes').value
            };
            
            let serverAddress;

            // Determinar el servidor SMTP según la opción seleccionada
            if (data.server == '1' || data.server.toLowerCase() === 'gmail') {
                serverAddress = "smtp.gmail.com";
                console.log("Servidor seleccionado: Gmail");
            } else if (data.server == '2' || data.server.toLowerCase() === 'yahoo') {
                serverAddress = "smtp.mail.yahoo.com";
                console.log("Servidor seleccionado: Yahoo");
            } else if (data.server == '3' || data.server.toLowerCase() === 'hotmail' || data.server.toLowerCase() === 'outlook') {
                serverAddress = "smtp-mail.outlook.com";
                console.log("Servidor seleccionado: Outlook/Hotmail");
            } else {
                console.error("Servidor no soportado");
                alert("Servidor no soportado");
                return;
            }

            console.log(`Iniciando envío de correos... Enviando ${data.nomes} correos al destino: ${data.to}`);

            // Enviar correos
            let no = 0;
            while (no < data.nomes) {
                try {
                    // Enviar el correo usando la librería SMTP.js
                    await Email.send({
                        Host: serverAddress,
                        Username: data.user,
                        Password: data.pwd,
                        To: data.to,
                        From: data.user,
                        Subject: data.subject,
                        Body: data.body
                    }).then(response => {
                        console.log(`Enviado ${no + 1} correo(s) de ${data.nomes}`);
                        no += 1;
                    }).catch(error => {
                        console.error(`Error al enviar el correo ${no + 1}:`, error);
                    });

                    if (no < data.nomes) {
                        // Esperar 0.8 segundos antes de enviar otro correo
                        console.log("Esperando 0.8 segundos antes de enviar el siguiente correo...");
                        await new Promise(resolve => setTimeout(resolve, 800));
                    }
                } catch (error) {
                    console.error("Error en el proceso de envío:", error);
                    break;
                }
            }

            if (no === data.nomes) {
                console.log("Todos los correos han sido enviados correctamente.");
            } else {
                console.error(`Se produjo un error al enviar todos los correos. Solo se enviaron ${no} correos.`);
            }
        });
