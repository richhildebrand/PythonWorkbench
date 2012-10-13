var workbenchViewModel  = new kendo.data.ObservableObject({
	UnitTests: new Array(),

	reset: function() {
		var tests = this.get("UnitTests");
		tests = new Array();
	},

	loadExpectedResults: function(tests) {
	this.reset()
	unitTests = this.get("UnitTests"); 
		for (var test in tests) {
			unitTests[test] = new UnitTest(tests[test]);
		}
	},

	loadActualResults: function(tests) {
		unitTests = this.get("UnitTests");
		for (var test in tests) {
			unitTests[test].actualResult = tests[test];
		} 
	},

	loadTestGridData: function() {
		unitTests = this.get("UnitTests")
		if (unitTests) {
			$('#TestResultGrid ol').empty();
			for (var unitTest in unitTests) {
				$('#TestResultGrid ol.testColumn').append('<li>' + unitTest.toString() + '</li>');
				$('#TestResultGrid ol.expectedResultColumn').append('<li>' +unitTests[unitTest].expectedResult + '</li>');
				$('#TestResultGrid ol.actualResultColumn').append('<li>' + unitTests[unitTest].actualResult + '</li>');
			}
		}
	}
});