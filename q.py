import re
from pathlib import Path

gradle_file = Path("app/build.gradle")
text = gradle_file.read_text()

deps = {
    "io.github.Rosemoe.sora-editor:editor": "0.23.4",
    "io.github.Rosemoe.sora-editor:language-textmate": "0.23.4",
    "com.android.tools:desugar_jdk_libs": "2.0.4"
}

# ------------------------
# cek dependencies
# ------------------------

for lib, ver in deps.items():

    pattern = rf"[\"']{lib}:[^\"']+[\"']"

    if re.search(pattern, text):
        # sudah ada tapi mungkin beda versi → ganti
        text = re.sub(
            pattern,
            f"'{lib}:{ver}'",
            text
        )
    else:
        # belum ada → tambahkan
        insert = f"implementation '{lib}:{ver}'"

        if "desugar_jdk_libs" in lib:
            insert = f"coreLibraryDesugaring '{lib}:{ver}'"

        text = re.sub(
            r"(dependencies\s*\{)",
            r"\1\n    " + insert,
            text,
            count=1
        )

# ------------------------
# aktifkan desugaring
# ------------------------

if "coreLibraryDesugaringEnabled true" not in text:

    if "compileOptions" in text:
        text = re.sub(
            r"(compileOptions\s*\{)",
            r"\1\n        coreLibraryDesugaringEnabled true",
            text,
            count=1
        )
    else:
        text = re.sub(
            r"(android\s*\{)",
            r"\1\n    compileOptions {\n        coreLibraryDesugaringEnabled true\n    }\n",
            text,
            count=1
        )

gradle_file.write_text(text)

print("✔ Dependencies checked / replaced / added")
