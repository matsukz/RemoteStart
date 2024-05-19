<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>

        <title>PCの電源をつける</title>
    </head>
    <body>
        
        <div class="d-flex justify-content-center align-items-center">
            <div class="col-7">

                <div class="text-center">
                    <h1>PCの電源をつける</h1>
                    <p>IPアドレスとMACアドレスを入力してください</p>
                </div>

                <div class="mb-3">
                    <label class="form-label">IPアドレス</label>
                    <input type="text" class="form-control" id="input_ip" name="input_ip" placeholder="192.168.XX.YY" maxlength=16>
                </div>

                <div class="mb-3">
                    <label class="form-label">MACアドレス</label>
                    <input type="text" class="form-control" id="input_mac" name="input_mac" placeholder="AB12CD34EF56" maxlength="12" minlength="12">
                </div>

                <div class="d-grid gap-2 col-6 mx-auto">
                    <button type="submit" class="btn btn-primary" id="exec">Weke Up</button>
                </div>

                <br><br>

                <!-- ココから下に結果を表示する -->
                <div id="progress"></div>
            
            </div>
        </div>

        <script src="main.js"></script>
        
    </body>
</html>