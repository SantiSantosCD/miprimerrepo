# miprimerrepo
Es un repositorio de ejemplo para aprender

# README — Cómo colaborar en este repositorio

**Resumen rápido**
Esta guía explica, de forma sencilla y práctica, cómo colaborar en este repositorio usando **SSH** (recomendado) o **fork + pull request** (recomendado para contribuciones públicas). Incluye los comandos que deben ejecutar tus colaboradores en Windows (Git Bash), macOS o Linux.

---

## Requisitos
- Cuenta en GitHub.
- Git instalado en la máquina local.
- (Recomendado) Configurar SSH en su máquina para autenticarse con GitHub.

---

## 1. Flujo recomendado para contribuciones
### Opción A — Con acceso de push (colaborador invitado)
1. Te añado como **colaborador** desde GitHub (Settings → Manage access → Invite a collaborator) y te doy permiso `Write`.
2. Tú generas una SSH key en tu máquina y la subes a tu cuenta de GitHub.
3. Clonas el repo por SSH y trabajas: `git clone git@github.com:TU_USUARIO/tu-repo.git`.
4. Haces cambios, commit y `git push` a la rama correspondiente.

### Opción B — Fork + Pull Request (para contribuyentes externos)
1. Forkea el repo (botón **Fork** en GitHub) a tu cuenta.
2. Clona tu fork: `git clone git@github.com:TU_USUARIO/FORK-REPO.git`.
3. Crea una rama, trabaja, push a tu fork y abre un **Pull Request** hacia el repo original.
4. El equipo revisa el PR y lo mergea (o pide cambios).

> Recomendación: para proyectos públicos o cuando no quieres dar acceso directo, usa **Fork + PR**.

---

## 2. Configurar SSH (comandos listos para copiar)
> Generar una clave por máquina; cada persona sube su clave pública a SU cuenta de GitHub. No compartas tu clave privada.

### Generar clave (Windows, macOS, Linux)
```bash
# Genera par de claves (ed25519 recomendado)
ssh-keygen -t ed25519 -C "tuemail@ejemplo.com"
# Acepta la ruta por defecto (Enter). Puedes poner passphrase o dejarlo vacío.
```

### Cargar clave en el agente SSH
```bash
# Inicia el agente
eval "$(ssh-agent -s)"
# Añade la clave privada (ajusta nombre si no es id_ed25519)
ssh-add ~/.ssh/id_ed25519
```

### Copiar la clave pública al portapapeles
- Windows (Git Bash):
```bash
cat ~/.ssh/id_ed25519.pub | clip
```
- macOS:
```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```
- Linux (con xclip):
```bash
cat ~/.ssh/id_ed25519.pub | xclip -sel clip
```

### Añadir clave en GitHub
- Entra a GitHub → Settings → SSH and GPG keys → New SSH key. Pega la clave pública y guarda.

---

## 3. Clonar, trabajar y enviar cambios (cheat sheet)
```bash
# Clonar por SSH
git clone git@github.com:TU_USUARIO/tu-repo.git
cd tu-repo

# Antes de trabajar, trae cambios remotos
git pull origin main

# Hacer cambios, añadir y confirmar
git add .
git commit -m "Mensaje claro del cambio"

# Subir los cambios
git push origin main
```

Si trabajas en una rama:
```bash
git checkout -b feature/mi-cambio
# hacer cambios
git add .
git commit -m "feat: ..."
git push origin feature/mi-cambio
```

---

## 4. Qué hago si veo errores comunes
- **Permission denied (publickey)**:  
  - Asegúrate de que tu clave pública está añadida a TU cuenta en GitHub y que `ssh-agent` tiene la clave cargada (`ssh-add -l`).
  - Verifica que el remote sea por SSH: `git remote -v` debe mostrar `git@github.com:...`.

- **403 al usar HTTPS**:  
  - Significa que las credenciales guardadas no tienen permiso. Borra credenciales guardadas y usa PAT o configura SSH.

- **Host key verification failed**:  
  - Puede que la huella del servidor cambió o haya un proxy. Usa `ssh-keyscan` para verificar la huella de `github.com` antes de aceptar.

---

## 5. Cómo invitar a colaboradores (para el propietario del repo)
1. Entra al repo → **Settings → Manage access**.
2. Click **Invite a collaborator**, escribe su usuario GitHub y envía la invitación.
3. Asigna el permiso `Write` si quieres que pueda hacer `push`.
4. El colaborador acepta la invitación desde su email o desde GitHub.

---

## 6. Buenas prácticas de seguridad
- Nunca compartas la clave privada (`~/.ssh/id_ed25519`).
- Cada máquina debe tener su propia clave. Subir varias claves a la misma cuenta es aceptable.
- Para contribuciones externas, usar **Fork + PR** permite revisión antes de merge.
- Revoca claves SSH en GitHub si alguien deja el proyecto.

---

## 7. Recursos y ayuda
- Si tienes problemas con SSH, pega la salida de:
```bash
ssh -vT git@github.com
```
- Si necesitas que te añada como colaborador, dame tu usuario GitHub y te invito.

---

¡Gracias por colaborar! Si quieres, puedo añadir este `README.md` directamente a tu repositorio (crearlo y hacer commit) — dime si lo hago y en qué rama lo quieres.

