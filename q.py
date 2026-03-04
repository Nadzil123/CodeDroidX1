import re
from pathlib import Path

gradle_file = Path("app/build.gradle")

text = gradle_file.read_text()

# 1. Tambahkan dependency Sora jika belum ada
if "sora-editor" not in text:
    text = re.sub(
        r"dependencies\s*\{",
        """dependencies {
    implementation 'io.github.Rosemoe.sora-editor:editor:0.23.4'
    implementation 'io.github.Rosemoe.sora-editor:language-textmate:0.23.4'
    coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:2.0.4'
""",
        text
    )

# 2. Aktifkan desugaring di compileOptions
if "coreLibraryDesugaringEnabled" not in text:
    text = re.sub(
        r"compileOptions\s*\{",
        """compileOptions {
        coreLibraryDesugaringEnabled true
""",
        text
    )

gradle_file.write_text(text)

print("✔ build.gradle updated")
