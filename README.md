# 🚨 Insecure Addon (For Testing Only)

This Odoo module is **intentionally insecure** and must **never be used in production**.  
It is designed **exclusively for testing security scanners and audit tools** in a safe, local development environment.

---

## ❗ Disclaimer

> This module contains serious security vulnerabilities introduced **on purpose**.  
> **DO NOT deploy this on any production or internet-facing instance.**

By using this module, you agree that:

- You are responsible for where and how you install it.
- It is intended for **educational and QA purposes only**.
- The authors and distributors are not liable for any misuse or consequences.

---

## ✅ Included Vulnerabilities (for scanner coverage)

| Vulnerability Type        | Description |
|---------------------------|-------------|
| Missing ACLs              | No `ir.model.access.csv` file |
| Permissive Record Rule    | Grants full access without domain |
| Unsafe SQL                | Manual SQL with string interpolation |
| Use of `eval()`           | With potentially unsanitized input |
| QWeb XSS Risk             | Uses `t-raw` with unescaped content |

---

## 📦 Installation

This module requires no dependencies beyond `base`. To install:

```bash
# Copy to your Odoo addons path
# Then upgrade or install manually:
./odoo-bin -u insecure_addon -d your_database
