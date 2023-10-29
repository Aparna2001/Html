function calculation()
{
var n1=parseInt(document.getElementById('fn').value);
var n2=parseInt(document.getElementById('sd').value);
var o=document.getElementById('opt').value;
// console.log(o);
// console.log(typeof o);
var a;
switch(o)
{
    case '+':   a=n1+n2;
                break;
    case '-':   a=n1-n2;
                break;
    case '*':   a=n1*n2;
                break;
    case '/':   a=n1/n2;
                break;
    case '%':   a=n1%n2;
                break;
    default:    break;
}
document.write(a);
}