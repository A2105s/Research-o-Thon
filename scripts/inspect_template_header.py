import fitz

doc = fitz.open('output/test_authors.pdf')
page = doc[0]
print("=== TEST_AUTHORS.PDF HEADER ===")
for b in page.get_text('dict')['blocks']:
    if b.get('type') == 0:
        for l in b['lines']:
            text = ' '.join([s['text'] for s in l['spans']]).strip()
            if l['bbox'][1] < 220:
                print(f"y={l['bbox'][1]:.1f}, x={l['bbox'][0]:.1f}: {text}")
