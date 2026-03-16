---
name: forensics-investigation
description: Pedagogical framework for digital forensics CTF challenges. Covers memory forensics, network captures, steganography, file carving, disk imaging, and log analysis. Enforces triage-before-extraction.
allowed-tools: Read, Bash, Glob, Python
---

# Forensics Investigation

> Every file tells a story. Your job is to read it without corrupting the evidence.

---

## 1. The Forensic Analysis Pipeline

**Core principle: Triage before extraction. Never modify the original evidence.**

### Phase A: Evidence Identification

1. Run `file <artifact>` to confirm the actual format
2. Classify the evidence type:

| Evidence Type | File Indicators | Primary Tool |
|:---|:---|:---|
| **Network capture** | `.pcap`, `.pcapng` | Wireshark / tshark |
| **Memory dump** | `.raw`, `.vmem`, `.dmp` | Volatility 3 |
| **Disk image** | `.dd`, `.e01`, `.img` | Autopsy / FTK Imager |
| **Image (stego)** | `.png`, `.jpg`, `.bmp` with unusual size | steghide, zsteg, binwalk |
| **Archive** | `.zip`, `.tar.gz`, `.7z` | Inspect before extracting |
| **Log files** | `.log`, `.evtx`, `.json` | grep, jq, timeline analysis |
| **PDF / Office** | `.pdf`, `.docx`, `.xlsx` | exiftool, oletools |
| **SQLite DB** | `.db`, `.sqlite` | sqlite3 CLI |

3. **Pedagogical Action:** Student identifies the evidence type and predicts what information it might contain

### Phase B: Metadata & Surface Analysis

1. Run `exiftool <file>` for metadata (author, dates, GPS, software)
2. Run `strings -n 6 <file>` for readable content
3. Run `binwalk <file>` (without `-e`) to map embedded data
4. Check file size vs expected size — steganography may inflate the file
5. **Pedagogical Action:** Explain what each piece of metadata reveals

### Phase C: Deep Analysis (Evidence-Type Specific)

See sections 2-6 below for specific methodologies.

### Phase D: Evidence Reconstruction

1. Piece together findings into a coherent narrative
2. Create a timeline of events (if applicable)
3. Document the chain of evidence
4. **Pedagogical Action:** Student constructs the narrative before the professor confirms

---

## 2. Network Forensics (PCAP/PCAPNG)

**Steps:**
1. Open in Wireshark → Statistics → Protocol Hierarchy (what protocols are present?)
2. Check for HTTP requests: `http.request.method == "GET" || http.request.method == "POST"`
3. Follow TCP streams: Right-click → Follow → TCP Stream
4. Export objects: File → Export Objects → HTTP/SMTP/etc.
5. Look for credentials: `ftp`, `telnet`, `http` (unencrypted)
6. DNS queries: `dns.qry.name` — check for DNS exfiltration

**Key filters:**
```
http.request.uri contains "flag"
tcp.port == 4444
dns.qry.name contains "suspicious"
ftp-data
smtp
```

**Pedagogical Action:** "What protocols do you see? Which ones transmit data in cleartext?"

---

## 3. Memory Forensics (Volatility)

**Steps:**
1. Identify the profile: `vol -f <dump> windows.info` or `linux.info`
2. List processes: `vol -f <dump> windows.pslist` or `windows.pstree`
3. Check network connections: `vol -f <dump> windows.netscan`
4. Dump suspicious process: `vol -f <dump> windows.dumpfiles --pid <PID>`
5. Check command history: `vol -f <dump> windows.cmdline`
6. Extract registry hives: `vol -f <dump> windows.hivelist`

**Common plugins (Volatility 3):**

| Plugin | Purpose |
|:---|:---|
| `windows.pslist` | List running processes |
| `windows.pstree` | Process tree (parent-child) |
| `windows.netscan` | Network connections |
| `windows.cmdline` | Command line arguments |
| `windows.filescan` | Scan for file objects |
| `windows.dumpfiles` | Extract files from memory |
| `windows.hashdump` | Extract password hashes |
| `windows.malfind` | Find injected code |

**Pedagogical Action:** "Looking at the process tree, which process seems out of place? Why?"

---

## 4. Steganography

**Detection checklist:**
1. Is the file size larger than expected for its dimensions/content?
2. Does `binwalk` find embedded files?
3. Does `exiftool` show unusual metadata?
4. Does `strings` reveal hidden text?

**Tools by image type:**

| Format | Tool | Command |
|:---|:---|:---|
| PNG | `zsteg` | `zsteg image.png` |
| JPG | `steghide` | `steghide extract -sf image.jpg` |
| Any | `binwalk` | `binwalk -e image.png` |
| Any | `stegsolve` | GUI — cycle through color planes |
| BMP | `stegsolve` | LSB analysis |

**Audio steganography:**
- `Audacity` — spectrogram view (visual messages in frequency domain)
- `sonic-visualiser` — detailed spectral analysis

---

## 5. File Carving

When data is deleted or hidden within another file:

1. `binwalk <file>` — identify embedded file offsets
2. `foremost <file>` — automated carving of known file types
3. `dd if=<file> bs=1 skip=<offset> count=<size> of=extracted` — manual extraction
4. **Pedagogical Action:** Explain what file carving does — recovering files from raw data without filesystem metadata

---

## 6. Disk Image Analysis

1. Mount the image read-only: `mount -o ro,loop image.dd /mnt/evidence`
2. Check deleted files: `fls -r image.dd` (Sleuth Kit)
3. Create timeline: `fls -r -m "/" image.dd | mactime -b -`
4. Open in Autopsy for GUI-based investigation
5. **Pedagogical Action:** "Why do we mount read-only? What happens if we modify the evidence?"

---

## 7. Bilingual Pedagogical Prompts

### PT-BR
- "Antes de extrair qualquer coisa, o que o `file` nos diz sobre esse artefato?"
- "Olhe a hierarquia de protocolos no Wireshark. Quais protocolos transmitem dados em texto claro?"
- "Esse processo parece suspeito na arvore de processos. Por que?"
- "O tamanho do arquivo e maior do que esperado. O que isso pode indicar?"

### EN
- "Before extracting anything, what does `file` tell us about this artifact?"
- "Look at the protocol hierarchy in Wireshark. Which protocols transmit data in cleartext?"
- "This process looks suspicious in the process tree. Why?"
- "The file size is larger than expected. What might this indicate?"

---

## 8. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
|:---|:---|
| Extract everything with `binwalk -e` immediately | Map contents first with `binwalk` (no `-e`), explain the layout |
| Modify the original evidence | Always work on a copy; mount read-only |
| Skip metadata analysis | Always run `exiftool` — metadata is often the clue |
| Ignore protocol hierarchy in PCAPs | Start with statistics → protocol hierarchy → then filter |
| Dump all memory without targeting | Identify suspicious processes first, then dump selectively |
