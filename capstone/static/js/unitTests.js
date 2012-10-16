var UnitTest = function(name, expectedResult) {
	this.name = name;
	this.expectedResult = expectedResult;
	this.actualResult = "";
};

var Exercise = function() {
	this.wordProblem = ""
	this.methodBody = "";
	this.methodCallText = "";

	this.currentLineNumber = 0;
	this.currentState = "";
	this.UnitTests = new Array();
}