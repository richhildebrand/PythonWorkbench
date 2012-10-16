$('#DisplayAllExercises').click(function() {
	$.get('/Exercise/displayAll/', function(data) {
		displayExercises(data)
	});
});

var displayExercises = function(data) {
	$('#Exercises').html(data);
	$('#Exercises').dialog();
	
};

$('.exercise').click(function() {
	var id = $(this).data('exerciseid');
	$.get('/Exercise/load/' + id, function(exercise) {
		loadExercise(exercise);
	});
});

var loadExercise = 	function(exercise) {
	clearAll();
	var methodBody = exercise.MethodBody
	var methodCalls = exercise.MethodCalls

	var methodCallText = "";
	for (var method in methodCalls) {
		methodCallText += method.toString() + "\n";
	};

	workbenchViewModel.loadNewExercise(exercise.WordProblem, methodBody, methodCallText);
	workbenchViewModel.loadExpectedResults(methodCalls);
	loadAllData(methodBody, methodCallText, methodCalls);
	$('#Exercises').dialog('close')
};