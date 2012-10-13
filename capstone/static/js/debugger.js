$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	loadAllData(methodBody, "");
});

$('#ClearAll').click(function() {
	clearAll();
});

var clearAll = function() {
	$('#TestResultGrid ol').empty();
	$('#ResultData').text("");
}

var loadAllData = function(methodBody, unitTestsText, unitTests) {
	clearAll();
	$('#PythonCode').val(methodBody);
	$('#MethodCalls').val(unitTestsText);
	loadTestGridData()
};

$('#startDebugging').click(function() {
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

var displayResultData = function(data) {
	$('#ResultData').text(data.exception + data.localVars + data.lineNumber);
	if (data.testResults) {
		loadActualResults(data.testResults);
		loadTestGridData();
	}
};