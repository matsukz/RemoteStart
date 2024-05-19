//Buttonを押したときに発動する
document.getElementById("exec").onclick = function(){
    //ロード画面表示
    $('#progress').html(`
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            データを取得中…
        </div>
    `);
};