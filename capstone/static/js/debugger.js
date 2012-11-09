$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	clearAll();
	pythonCodeEditor.setValue(methodBody);
	loadAllData(methodBody, "");
});

$('#ClearAll').click(function() {
	clearAll();
});

var clearAll = function() {
	$('#PythonCode').val("");
	$('#MethodCalls').val("");
	$('#ResultData').text("");
	pythonCodeEditor.setValue("");
	unitTestEditor.setValue("");
	workbenchViewModel.reset();
}

var loadAllData = function(methodBody, unitTestsText, unitTests) {
	$('#PythonCode').val(methodBody);
	$('#MethodCalls').val(unitTestsText);
};

$('#startDebugging').click(function() {
	pythonCodeEditor.save();
	var pythonCode = { pythonCode: $('#PythonCode').val(), unitTests: $('#MethodCalls').val() };
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
	var pythonCode = { pythonCode: $('#PythonCode').val(), unitTests: $('#MethodCalls').val() };
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