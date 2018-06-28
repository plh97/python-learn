// function bind_(fn,context,...argsOut){
// 	return function (...argsInn){
// 		return fn.apply(context, [...argsOut,...argsInn])
// 	}
// }
// function a(b){
// 	console.log(this,b);
// }




// ;(function (){
// 	a.bind('this',['234','234'] )()
// 	// console.log(this);
// })()

var arr = [
	{name:'xiaoming',id:"123"},
	{name:'xiaoming',id:"456"},
	{name:'xiaoming',id:"789"},
	{name:'xiaohua',id:"101112"},
	{name:'xiaowang',id:"131415"},
	{name:'xiaohong',id:"161718"}
];

res = arr.filter(e=>e.name==='xiaoming').reduce((all,e)=>{
	return {name: 'xiaoming',id:[...all.id , e.id]}
},{name:'xiaoming',id:[]})

console.log(res);