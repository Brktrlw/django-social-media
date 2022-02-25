function likePostFunc(slug) {

    var btn=document.getElementById(slug);
    if(btn.className == "btn btn-outline-danger"){
        // beğenmemişse (beğenirken)
        var spanlike=document.getElementById("likecount-"+slug);
        var totalLike=spanlike.getAttribute("count");
        var yenideger=parseInt(totalLike)+1;
        spanlike.setAttribute("count",yenideger);
        spanlike.textContent=yenideger+" Beğeni";
        var url = '/like/postlike/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken
            },
            body: JSON.stringify({
                'slug':slug
            })
        })
        btn.className="btn btn-danger"
    }
    else{
        //beğeniyi geri çekiyor
        var spanlike=document.getElementById("likecount-"+slug);
        var totalLike=spanlike.getAttribute("count");
        var yenideger=parseInt(totalLike)-1;
        spanlike.setAttribute("count",yenideger);
        spanlike.textContent=yenideger+" Beğeni";
        var url = '/like/postlike/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken
            },
            body: JSON.stringify({
                'slug':slug
            })
        })
        btn.className="btn btn-outline-danger"
    }




}
