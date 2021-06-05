document.addEventListener("DOMContentLoaded",myfunction);
    function myfunction()
    {
        
        const queryString=window.location.search;
        const urlParams=new URLSearchParams(queryString);
        if(urlParams.has('success'))
        {
            alert("signed up successfully");
        }

    }
 