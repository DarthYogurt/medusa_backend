
var currId = 0;



function addCreateStep(idNum){
	
	var stepNum = document.createElement("label");
	stepNum.className = "col-md-1 control-label";
	stepNum.innerHTML = idNum;
	
	var stepInput = document.createElement("input");
	stepInput.name = "name";
	
	stepInput.id = "newStepId"+idNum;
	
	var selectType = document.createElement("select");
	selectType.className = "form-control";
	
	
	var formGroup = document.createElement("div");
	formGroup.className = "form-group form-inline";
	formGroup.id = "groupStepId"+idNum;
	formGroup.appendChild(stepNum);
	formGroup.appendChild(stepInput);
	formGroup.appendChild(selectType);
	
	
	var createStepsDiv = document.getElementById("create-steps");
	
	createStepsDiv.appendChild(formGroup);
};

function deleteStep(){
	var createSteps = document.getElementById("create-steps");
	createSteps.removeChild(document.getElementById("groupStepId"+currId));
}





addCreateStep(currId);

$("#removeStep").click(function() {
	deleteStep();
	currId --;
});

$("#addStep").click(function() {
	currId ++;						 
	addCreateStep(currId);
	
	
});


