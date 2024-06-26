//Buttonを押したときに発動する
document.getElementById("exec").onclick = function(){
    
    //ドメイン取得
    var url = new URL(window.location.href);
    var api = url.protocol + "//" + url.hostname + "/api/wol/"
    var mac = document.getElementById("input_mac").value;
    var ip = document.getElementById("input_ip").value;

    //必要な値がないとこの先は進まない
    if (mac == "" || ip == "") {
        alert("必要な値が入力されていません");
        return false;
    }

    //関数にしないとボタンが無効にならない
    function btn_disable(type){
        var button = document.getElementById('exec');
        button.disabled = type;        
    }

    //ボタン無効化
    btn_disable(true);    

    console.log(api);
    console.log(mac);
    console.log(ip);

    //ロード画面表示
    $('#progress').html(`
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            シグナル送信中…
        </div>
    `);

    //APIサーバーと通信する
    $.ajax({
        url: api,
        type: "POST",
        contentType: 'application/json', // コンテントタイプ
        accept: 'application/json', // 受け入れるレスポンスのタイプ
        data: JSON.stringify({"mac": mac, "ip": ip }),
        timeout: 10000000
    }).done(function(response) {
        //通信が成功してレスポンスが返ってきたとき
        var message = "";
        console.log(response);
            switch (response["msg"]) {
            case 0:
                message = "起動しました！";
                break;
            case 1:
                message = "起動シグナルを送信しましたが応答がありません。";
                break;
            case 2:
                message = "起動シグナルの送信に失敗しました。";
            default:
                message = "起動シグナルの送信に失敗しました。";
        }
        
        //メッセージ表示
        $('#progress').html(`<p class=text-center>` + message + `<p>`);

    }).fail(function() {
        //通信できなかったとき
        $('#progress').html(`<p class=text-center>APIサーバーと通信できません。<p>`);
    });

    //どっちにしてもButtonは有効にする
    btn_disable(false);

};