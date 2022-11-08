







val inputDf = spark.read('')
// input df schema {empId,empName,empDept,empAge,empSlary,empGnder}


//let say we want to update gender & salary , we use Map to interate over a dataframe at row level and use copy operation to copy fields that are 
// not modified and use assign new value to update value 

//we are using MAP to iterate the dataFrame
val updatedDf = inputDf. map (
                                row=>{
                                
                                  //updating M to Male , F to Female
                                val gender = if( row.empGender == 'M') "MALE" else "FEMALE"
                                  
                                  //just adding 5k to current salary
                                 val salary = row.empSalary + 5000
                                }
  
                      // we are using the copy operation to take all unedited columns as is and we are updating the columns where we want to update
                              row.copy(
                                 empGender = gender,
                                 empSalary = salary 
                              )
                              )
