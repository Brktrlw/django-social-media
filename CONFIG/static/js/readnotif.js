function readNotifFunc() {
    try {
        var notifcount = document.getElementById("notifcount").textContent
        if (notifcount != "" | notifcount == null) {
            var url = '/notification/readallnotif/'



            const csrftoken = getCookie('csrftoken');
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
            }).then(() => {
                try {
                    var notifBadge = document.getElementById("notifcount");
                    notifBadge.remove();

                } catch (e) {

                }

            })
        }
    } catch (e) {
        var notifContent = document.getElementsByClassName("notifContent");
        for (var i = 0; i < notifContent.length; i++) {
            notifContent[i].style.fontWeight = "";
        }
    }


}