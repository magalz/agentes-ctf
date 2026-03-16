---
name: cryptography-analysis
description: Pedagogical framework for cryptographic CTF challenges. Covers classical ciphers, RSA, AES, ECC, hash attacks, and mathematical foundations. Enforces understanding before automation.
allowed-tools: Read, Bash, Glob, Python
---

# Cryptography Analysis

> Understand the math before you break it. Every cipher has a weakness if you know where to look.

---

## 1. The Crypto Analysis Pipeline

### Phase A: Cipher Identification

Before running any tool, identify what you're working with:

| Signal | Likely Cipher Type |
|:---|:---|
| Long hex string, repeating patterns | XOR or substitution cipher |
| Base64 with standard padding (`=`) | Encoding, not encryption |
| Large integers (n, e, c) | RSA |
| Hex blocks of 16/32 bytes | AES (ECB or CBC) |
| Short repeating key pattern | Vigenere or repeating XOR |
| Frequency analysis matches language | Monoalphabetic substitution |
| `.pem` file with "BEGIN PUBLIC KEY" | RSA public key |
| Random-looking binary blob | Check for known cipher headers |

**Pedagogical Gate:** Student must identify the cipher type before any cracking attempt.

### Phase B: Mathematical Foundation

Explain the relevant math before exploitation:

| Cipher | Core Concept to Teach |
|:---|:---|
| **RSA** | Modular arithmetic, Euler's totient, factoring hardness |
| **AES-ECB** | Block cipher modes, why ECB leaks patterns |
| **AES-CBC** | IV importance, padding oracle mechanism |
| **XOR** | XOR properties: A XOR A = 0, A XOR 0 = A |
| **Diffie-Hellman** | Discrete logarithm problem, small subgroup attacks |
| **ECC** | Point addition, scalar multiplication, invalid curve |
| **Hashing** | One-way function, collision vs preimage resistance |

### Phase C: Attack Execution

Select attack based on identified weakness:

### Phase D: Verification

Student must explain why the attack worked mathematically.

---

## 2. Attack Reference by Category

### Classical Ciphers

| Cipher | Attack | Tool |
|:---|:---|:---|
| Caesar | Brute force (25 rotations) | Manual or CyberChef |
| Substitution | Frequency analysis | quipqiup.com or manual |
| Vigenere | Kasiski examination → key length → frequency per block | CyberChef or manual |
| XOR | Known-plaintext (if partial known), frequency if short key | Python script |

### RSA Attacks

| Weakness | Attack | Condition |
|:---|:---|:---|
| Small `n` | Factor directly | n < 100 digits → FactorDB |
| Small `e` (e=3) | Coppersmith / cube root | c = m^e < n (no modular reduction) |
| Large `e` | Wiener's attack | e > n^0.25 approximation |
| Shared `p` or `q` | GCD across multiple keys | Two keys share a factor |
| Low public exponent + same message | Hastad's broadcast attack | Same m encrypted with e different keys |
| Padding oracle | Bleichenbacher | Chosen-ciphertext access |
| Known factorization | Direct decryption | p, q are known or factorable |

**RSA Decryption Steps:**
```python
# When p, q are known:
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)        # modular inverse
m = pow(c, d, n)            # decrypt
plaintext = m.to_bytes(length, 'big')
```

### AES Attacks

| Mode | Weakness | Attack |
|:---|:---|:---|
| **ECB** | Identical blocks produce identical ciphertext | Block manipulation, chosen-plaintext |
| **CBC** | Padding oracle, bit-flipping | Padding oracle attack, IV manipulation |
| **GCM** | Nonce reuse | Forbidden attack (nonce reuse → key recovery) |

### Hash Attacks

| Attack | Description | Tools |
|:---|:---|:---|
| **Brute force** | Try all inputs | `hashcat`, `John the Ripper` |
| **Rainbow tables** | Precomputed hash lookups | CrackStation, online DBs |
| **Length extension** | Extend hash without knowing secret | `hash_extender`, `HashPump` |
| **Collision** | Find two inputs with same hash | Specific to MD5/SHA1 (known collisions) |

---

## 3. Essential Tools

| Tool | Purpose | When to Use |
|:---|:---|:---|
| `CyberChef` | Encoding/decoding, cipher ops | First stop — visual transformations |
| `SageMath` | Mathematical crypto attacks | RSA, ECC, lattice-based attacks |
| `RsaCtfTool` | Automated RSA attacks | When RSA parameters are available |
| `FactorDB` | Integer factorization database | Check if `n` is already factored |
| `openssl` | Key parsing, encryption/decryption | Examining certificates and keys |
| `hashcat` / `John` | Hash cracking | When hashes are discovered |
| `hash_extender` | Hash length extension | When MAC uses H(secret + message) |

---

## 4. Bilingual Pedagogical Prompts

### PT-BR
- "Antes de tentar quebrar, identifique: que tipo de cifra estamos enfrentando?"
- "Por que o RSA e seguro normalmente? O que faz este caso ser vulneravel?"
- "O que o modo ECB faz de diferente do CBC? Por que isso e um problema?"
- "Explique matematicamente por que o ataque de Wiener funciona com expoentes grandes."

### EN
- "Before trying to crack it, identify: what type of cipher are we facing?"
- "Why is RSA normally secure? What makes this case vulnerable?"
- "What does ECB mode do differently from CBC? Why is that a problem?"
- "Explain mathematically why Wiener's attack works with large exponents."

---

## 5. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
|:---|:---|
| Use RsaCtfTool without understanding the attack | Identify the weakness first, explain the math, then use the tool |
| Skip frequency analysis for classical ciphers | Always try frequency analysis before automated cracking |
| Ignore the cipher mode (ECB vs CBC) | Mode determines the attack — identify it first |
| Brute-force without analyzing parameters | Check for mathematical weaknesses before brute force |
