function deneme() {
    try {
       var notifcount = document.getElementById("notifcount").textContent
         if (notifcount != "" | notifcount==null) {
        var url = '/notification/readallnotif/'

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        const csrftoken = getCookie('csrftoken');
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
        }).then(() => {
            try {
                 var notifBadge=document.getElementById("notifcount");
                notifBadge.remove();
            }
            catch (e) {

            }

            })
    }
    }
    catch (e) {

    }


}