var pythonCodeEditor = CodeMirror.fromTextArea(document.getElementById("PythonCode"), {
  mode: "text/x-python",
  lineNumbers: true,
  lineWrapping: true,
  theme: "neat",
  onChange: function() {
    unitTestEditor.setOption("firstLineNumber", pythonCodeEditor.lineCount() + 1);
  }
});

var unitTestEditor = CodeMirror.fromTextArea(document.getElementById("MethodCalls"), {
  mode: "text/x-python",
  lineNumbers: true,
  lineWrapping: false,
  theme: "neat",
  readOnly: true,
  firstLineNumber : pythonCodeEditor.lineCount() + 1
});

var currentLine = {   
                    line:pythonCodeEditor.getLineHandle(0),
                    isUserCodeLine: true
                  };