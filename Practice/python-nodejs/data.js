let {PythonShell} = require('python-shell')

let options = {args:["40.9652857", "29.0595285", "5", "2022-07-01T00:00:00", "2022-07-22T00:00:00", "ND,PD,HUM_ibb,NO_ibb,PD", "daily"]}

PythonShell.run("public/python_utils/get_data/main.py", options, function(err, results){
    console.log(results[0])
})


