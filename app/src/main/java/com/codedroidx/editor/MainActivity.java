package com.codedroidx.editor;

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

        editor.setText("// CodeDroidX IDE\n");
    }
}
