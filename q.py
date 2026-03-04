import re
from pathlib import Path

# -------------------
# FILE PATHS
# -------------------

gradle = Path("app/build.gradle")
layout = Path("app/src/main/res/layout/activity_main.xml")
main = Path("app/src/main/java/com/codedroidx/editor/MainActivity.java")

# -------------------
# UPDATE GRADLE
# -------------------

text = gradle.read_text()

deps = [
"implementation 'io.github.Rosemoe.sora-editor:editor:0.23.4'",
"implementation 'io.github.Rosemoe.sora-editor:language-textmate:0.23.4'",
"coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:2.0.4'"
]

for dep in deps:
    if dep not in text:
        text = re.sub(r"(dependencies\s*\{)", r"\1\n    "+dep, text, count=1)

if "coreLibraryDesugaringEnabled true" not in text:
    text = re.sub(
        r"(compileOptions\s*\{)",
        r"\1\n        coreLibraryDesugaringEnabled true",
        text,
        count=1
    )

gradle.write_text(text)

# -------------------
# UPDATE LAYOUT
# -------------------

layout_content = """<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:orientation="vertical"
android:layout_width="match_parent"
android:layout_height="match_parent">

<com.google.android.material.tabs.TabLayout
android:id="@+id/tabs"
android:layout_width="match_parent"
android:layout_height="wrap_content"/>

<io.github.rosemoe.sora.widget.CodeEditor
android:id="@+id/editor"
android:layout_width="match_parent"
android:layout_height="0dp"
android:layout_weight="1"/>

</LinearLayout>
"""

layout.write_text(layout_content)

# -------------------
# UPDATE MAIN ACTIVITY
# -------------------

main_code = """package com.codedroidx.editor;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import com.google.android.material.tabs.TabLayout;
import io.github.rosemoe.sora.widget.CodeEditor;

public class MainActivity extends AppCompatActivity {

    CodeEditor editor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editor = findViewById(R.id.editor);

        // Auto indent
        editor.setAutoIndent(true);

        // Tab width
        editor.setTabWidth(4);

        editor.setText("// CodeDroidX IDE\\n");
    }
}
"""

main.write_text(main_code)

print("✔ Editor upgrade complete")
