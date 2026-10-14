import subprocess
import fitz
from PIL import Image
import io

with open('manuscript/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Current author block
current_author = r"""\author{
\IEEEauthorblockN{Parikshit Singh Bais, Adarsh Singh, Sourav, and Anamidhi Shrivastava}
\IEEEauthorblockA{\textit{Department of Computer Science and Engineering}\\
\textit{Amity School of Engineering and Technology, Amity University Madhya Pradesh}\\
Gwalior, Madhya Pradesh, India\\
Email: \{parikshit.bais, adarsh.singh, sourav, anamidhi.shrivastava\}@amity.edu}
}"""

# 2-col author block matching template (2).pdf
author_2col = r"""\author{
\IEEEauthorblockN{Parikshit Singh Bais, Adarsh Singh}
\IEEEauthorblockA{\textit{dept. of Computer Science and Engineering}\\
Amity School of Engineering and Technology\\
Amity University Madhya Pradesh\\
Gwalior, India\\
e-mail: \{parikshit.bais, adarsh.singh\}@amity.edu}
\and
\IEEEauthorblockN{Sourav, Anamidhi Shrivastava}
\IEEEauthorblockA{\textit{dept. of Computer Science and Engineering}\\
Amity School of Engineering and Technology\\
Amity University Madhya Pradesh\\
Gwalior, India\\
e-mail: \{sourav, anamidhi.shrivastava\}@amity.edu}
}"""

old_title = r"\title{Sovereign by Design: An Integrated Five-Pillar Framework\\for India's Strategic Compute and Artificial Intelligence Infrastructure}"
new_title = r"\title{\textbf{Sovereign by Design: An Integrated Five-Pillar Framework\\for India's Strategic Compute and Artificial Intelligence Infrastructure}}"

bold_title_text = text.replace(current_author, author_2col).replace(old_title, new_title)

with open('manuscript/test_bold_title_2col.tex', 'w', encoding='utf-8') as f:
    f.write(bold_title_text)

subprocess.run(['pdflatex', '-interaction=nonstopmode', 'test_bold_title_2col.tex'], cwd='manuscript', capture_output=True)
subprocess.run(['bibtex', 'test_bold_title_2col'], cwd='manuscript', capture_output=True)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'test_bold_title_2col.tex'], cwd='manuscript', capture_output=True)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'test_bold_title_2col.tex'], cwd='manuscript', capture_output=True)

doc = fitz.open('manuscript/test_bold_title_2col.pdf')
print('Page count:', len(doc))
print('Last page characters:', len(doc[-1].get_text()))
pix = doc[0].get_pixmap(dpi=150)
w, h = pix.width, pix.height
img = Image.open(io.BytesIO(pix.tobytes()))
crop = img.crop((0, 0, w, int(h * 0.35)))
crop.save('C:/Users/Parikshit/.gemini/antigravity-ide/brain/3392610e-be84-42e8-b4fa-f4fd6db01632/bold_title_2col_header.png')
print('Saved bold_title_2col_header.png successfully!')
