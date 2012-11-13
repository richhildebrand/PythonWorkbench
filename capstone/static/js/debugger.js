$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	clearAll();
	loadAllData(methodBody, "");
});

$('#ClearAll').click(function() {
	clearAll();
});

var clearAll = function() {
	$('#PythonCode').val("");
	$('#MethodCalls').val("");
	$('#ResultData').text("");
	workbenchViewModel.reset()
}

var loadAllData = function(methodBody, unitTestsText, unitTests) {
	$('#PythonCode').val(methodBody);
	$('#MethodCalls').val(unitTestsText);
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
	$('#ResultData').text(data.exception + data.localVars + data.good_stuff);
	if (data.testResults) {
		workbenchViewModel.loadActualResults(data.testResults);
	}
};