$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	clearAll();
	loadEditorText(methodBody, "");
});

$('#ClearAll').click(function() {
	clearAll();
});

var clearAll = function() {
	$('#ResultData').text("");
	pythonCodeEditor.setValue("");
	unitTestEditor.setValue("");
	workbenchViewModel.reset();
}

var loadEditorText = function() {
	pythonCodeEditor.setValue(workbenchViewModel.userCodeSegment);
	unitTestEditor.setValue(workbenchViewModel.getMethodCallTextFromUnitTests());
};

$('#startDebugging').click(function() {
	var pythonCode = { pythonCode: pythonCodeEditor.getValue, unitTests: unitTestEditor.getValue() };
	$.get('/student/startDebugging', pythonCode, function(data) {
		displayResultData(data)
	});
});

$("#TakeStep").click(function() {
  $.get('/student/takeStep', function(data) {
		displayResultData(data)
	});
});

$('#runAll').click(function() {
	var pythonCode = { pythonCode: pythonCodeEditor.getValue, unitTests: unitTestEditor.getValue() };
	$.get('/student/runAll', pythonCode, function(data) {
		displayResultData(data)
	});
});

var displayResultData = function(data) {
	$('#ResultData').text(data.exception + data.localVars);
	if (data.testResults) {
		workbenchViewModel.loadActualResults(data.testResults);

	}
	workbenchViewModel.highlightCurrentLine(parseInt(data.lineNumber));
};