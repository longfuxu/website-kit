"""Build the workshop page (10 slides + follow-along kit) from src/site.src.html.
Injects master-prompt.txt, academic-website/SKILL.md and src/qr.svg.
Writes kit/index.html (standalone, served by GitHub Pages) and, if a path is given, an artifact copy
without the <html>/<head> wrapper."""
import html, re, sys, pathlib
kit = pathlib.Path(__file__).resolve().parent.parent
src = (kit / "src/site.src.html").read_text()
prompt = (kit / "master-prompt.txt").read_text().strip()
skill = (kit / "academic-website/SKILL.md").read_text().strip()
qr = (kit / "src/qr.svg").read_text().strip().replace(' aria-label=', ' role="img" aria-label=', 1)
p = html.escape(prompt, quote=False)
p = re.sub(r"\[(?!TODO)[^\]\n]*\]", lambda m: f'<span class="fill">{m.group(0)}</span>', p)
page = (src.replace("<!--MASTER_PROMPT-->", p)
           .replace("<!--SKILL_MD-->", html.escape(skill, quote=False))
           .replace("<!--QR_SVG-->", qr))
assert "<!--MASTER_PROMPT-->" not in page and "<!--QR_SVG-->" not in page
head, body = page.split("</style>", 1)
standalone = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
              '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
              + head + "</style>\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n")
(kit / "index.html").write_text(standalone)
(kit / ".nojekyll").write_text("")
if len(sys.argv) > 1:
    out = pathlib.Path(sys.argv[1]); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(page)
print("ok", len(standalone), "bytes; slides:", page.count('class="slide"'), "; copy buttons:", page.count('class="copy"'))
