$(document).ready(function () {
  // $("p").click(function(){
  //   $(this).hide();
  // });
  var getFile = document.getElementById("files");
  getFile.onchange = function (e) {
    //获取到文件以后就会返回一个对象，通过这个对象即可获取文件
    console.log(e.currentTarget.files);//所有文件，返回的是一个数组
    console.log(e.currentTarget.files[0].name)//文件名
    readMd(e.currentTarget.files[0]);
    // $("#mdContent").val(e.currentTarget.files[0]);
  }
});

function readMd(file) {
  var reader = new FileReader();
  //   if (/md+/.test(fileText.type)) {//判断文件类型，是不是text类型
  reader.onload = function () {
    $("#mdContent").val(this.result);
    var result = $("#mdContent").val();
    convertHtml(result);
    // console.log(result);
  }
  reader.readAsText(file);
}

function convertHtml(md) {
  var converter = new Markdown.Converter();
  var html = converter.makeHtml(md);
  $("#htmlContent").html(html);
  // var file = new File([html], "output/htmlContent.html", { type: "text/plain;charset=utf-8" });
  // saveAs(file);
}

