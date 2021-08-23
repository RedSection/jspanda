
var result = "jspanda test"

    var a = eval("window.__proto__.jspanda");

    if (a==="testpayload") {

        console.log("1")

        if (typeof a !== 'undefined') {

        console.log("Panda is happy ʕ -㉨- ʔ")

        result = "Panda is happy ʕ -㉨- ʔ"
    
	    }    

    } else {

        console.log("Panda is sad ʕ -㉨- ʔ")

        result = "Panda is sad ʕ -㉨- ʔ"

    }

return result
