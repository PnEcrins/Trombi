(function(e){function t(t){for(var r,i,s=t[0],a=t[1],l=t[2],d=0,b=[];d<s.length;d++)i=s[d],Object.prototype.hasOwnProperty.call(c,i)&&c[i]&&b.push(c[i][0]),c[i]=0;for(r in a)Object.prototype.hasOwnProperty.call(a,r)&&(e[r]=a[r]);u&&u(t);while(b.length)b.shift()();return o.push.apply(o,l||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],r=!0,s=1;s<n.length;s++){var a=n[s];0!==c[a]&&(r=!1)}r&&(o.splice(t--,1),e=i(i.s=n[0]))}return e}var r={},c={app:0},o=[];function i(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.m=e,i.c=r,i.d=function(e,t,n){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)i.d(n,r,function(t){return e[t]}.bind(null,r));return n},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],a=s.push.bind(s);s.push=t,s=s.slice();for(var l=0;l<s.length;l++)t(s[l]);var u=a;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"0937":function(e,t,n){},3209:function(e,t,n){},"37b9":function(e,t,n){e.exports=n.p+"img/camille.monchicourt.338966ca.jpg"},"3ec0":function(e,t,n){},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23");function c(e,t,n,c,o,i){var s=Object(r["j"])("TrombiCal");return Object(r["f"])(),Object(r["c"])(s,{msg:"Welcome to Your Vue.js App"})}var o=n("cf05"),i=n.n(o),s=n("fc5b"),a=n.n(s),l=Object(r["n"])("data-v-804c79dc");Object(r["h"])("data-v-804c79dc");var u={id:"wrapper"},d={id:"sidebar-wrapper"},b={class:"logo-container"},f={class:"sidebar-nav"},p={id:"page-content-wrapper"},h={class:"container-fluid"},j={key:0},O={class:"card mb-3"},v={class:"row g-0"},m={class:"col-md-2"},g={key:1,src:a.a,class:"img-fluid rounded-start",alt:"Pensez à ajouter une photo"},y={class:"col-md-10 no-padding"},U={key:0},P={class:"row"},k={class:"card align",style:{width:"18rem"}},w={key:1,width:"250",height:"200",src:a.a,class:"card-img-top",alt:"..."};Object(r["g"])();var C=l((function(e,t,c,o,s,a){var l,C,_=Object(r["j"])("UserCard"),M=Object(r["j"])("UserCalendar");return Object(r["f"])(),Object(r["c"])("div",u,[Object(r["e"])("div",d,[Object(r["e"])("div",b,[Object(r["e"])("img",{onClick:t[1]||(t[1]=function(t){return e.refresh()}),id:"logo",src:i.a})]),Object(r["e"])("h1",{id:"refresh",onClick:t[2]||(t[2]=function(t){return e.refresh()})},Object(r["k"])(e.$config.APP_NAME),1),Object(r["e"])("ul",f,[Object(r["m"])(Object(r["e"])("input",{class:"form form-control",placeholder:"Rechercher",type:"text",name:"search",id:"search","onUpdate:modelValue":t[3]||(t[3]=function(t){return e.searchPattern=t}),onInput:t[4]||(t[4]=function(){return e.filterUsers&&e.filterUsers.apply(e,arguments)})},null,544),[[r["l"],e.searchPattern]]),(Object(r["f"])(!0),Object(r["c"])(r["a"],null,Object(r["i"])(e.allUsers,(function(t,n){return Object(r["f"])(),Object(r["c"])("li",{key:t},[Object(r["e"])("a",{class:"dep",href:"#",onClick:function(t){return e.setCurrDepartment(n)}},Object(r["k"])(n),9,["onClick"]),(Object(r["f"])(!0),Object(r["c"])(r["a"],null,Object(r["i"])(t,(function(t){return Object(r["f"])(),Object(r["c"])("a",{class:"person",key:t,onClick:function(n){return e.setCurrentUser(t)}},Object(r["k"])(t.displayName),9,["onClick"])})),128))])})),128))])]),Object(r["e"])("div",p,[Object(r["e"])("div",h,[e.currentUser?(Object(r["f"])(),Object(r["c"])("div",j,[Object(r["e"])("h2",null," Fiche "+Object(r["k"])(null===(l=e.currentUser)||void 0===l?void 0:l.displayName),1),Object(r["e"])("div",O,[Object(r["e"])("div",v,[Object(r["e"])("div",m,[e.currentUser.has_photo?(Object(r["f"])(),Object(r["c"])("img",{key:0,src:n("b5a1")("./".concat(null===(C=e.currentUser)||void 0===C?void 0:C.sAMAccountName,".jpg")),class:"img-fluid rounded-start",alt:"..."},null,8,["src"])):(Object(r["f"])(),Object(r["c"])("img",g))]),Object(r["e"])("div",y,[Object(r["e"])(_,{user:e.currentUser,onHasPhoto:t[5]||(t[5]=function(t){return e.changeHasPhotoProp(t)}),displayAddPhoto:""},null,8,["user"])])])]),Object(r["e"])("div",null,[Object(r["e"])(M,{user:e.currentUser},null,8,["user"])])])):Object(r["d"])("",!0),(Object(r["f"])(!0),Object(r["c"])(r["a"],null,Object(r["i"])(e.filteredUsers,(function(c,o){return Object(r["f"])(),Object(r["c"])("div",{key:c},[c.length>0?(Object(r["f"])(),Object(r["c"])("div",U,[Object(r["e"])("h3",null,Object(r["k"])(o),1),Object(r["e"])("div",P,[(Object(r["f"])(!0),Object(r["c"])(r["a"],null,Object(r["i"])(c,(function(c){return Object(r["f"])(),Object(r["c"])("div",{class:"card-container",key:c},[Object(r["e"])("div",k,[c.has_photo?(Object(r["f"])(),Object(r["c"])("img",{key:0,src:n("b5a1")("./".concat(null===c||void 0===c?void 0:c.sAMAccountName,".jpg")),class:"card-img-top"},null,8,["src"])):(Object(r["f"])(),Object(r["c"])("img",w)),Object(r["e"])(_,{user:c,onSetUser:t[6]||(t[6]=function(t){return e.setCurrentUser(t)}),displaySeeMoreBtn:""},null,8,["user"])])])})),128))])])):Object(r["d"])("",!0)])})),128))])])])})),_=(n("d81d"),n("b64b"),n("159b"),n("4de4"),n("bc3a")),M=n.n(_),A=(n("a4d3"),n("e01a"),{class:"card-body no-padding-top"}),x={class:"card-title"},N={key:0},E={key:1},D={key:2},T={key:4},I=Object(r["e"])("br",null,null,-1),S={key:0,class:"custom-file"},B=Object(r["e"])("label",{class:"custom-file-label",for:"customFile"},"Ajouter ou modifier la photo",-1);function $(e,t,n,c,o,i){var s,a,l,u,d,b,f,p,h,j,O,v,m;return Object(r["f"])(),Object(r["c"])("div",A,[Object(r["e"])("h5",x,Object(r["k"])(null===(s=n.user)||void 0===s?void 0:s.displayName),1),(null===(a=n.user)||void 0===a||null===(l=a.description)||void 0===l?void 0:l.length)>0?(Object(r["f"])(),Object(r["c"])("div",N,Object(r["k"])(null===(u=n.user)||void 0===u?void 0:u.description[0]),1)):Object(r["d"])("",!0),null!==(d=n.user)&&void 0!==d&&d.homePhone&&(null===(b=n.user)||void 0===b||null===(f=b.homePhone)||void 0===f?void 0:f.length)>0?(Object(r["f"])(),Object(r["c"])("div",E," Téléphone bureau : "+Object(r["k"])(null===(p=n.user)||void 0===p?void 0:p.homePhone),1)):Object(r["d"])("",!0),null!==(h=n.user)&&void 0!==h&&h.mobile&&(null===(j=n.user)||void 0===j||null===(O=j.mobile)||void 0===O?void 0:O.length)>0?(Object(r["f"])(),Object(r["c"])("div",D," Téléphone portable : "+Object(r["k"])(null===(v=n.user)||void 0===v?void 0:v.mobile),1)):Object(r["d"])("",!0),Object(r["e"])("a",{href:"mailto: "+(null===(m=n.user)||void 0===m?void 0:m.mail),class:"btn btn-primary"},"Email",8,["href"]),n.displaySeeMoreBtn?(Object(r["f"])(),Object(r["c"])("button",{key:3,onClick:t[1]||(t[1]=function(e){return i.changeUser(n.user)}),class:"btn btn-outline-info ml-3"},"Voir plus")):Object(r["d"])("",!0),n.displayAddPhoto?(Object(r["f"])(),Object(r["c"])("div",T,[I,e.$config.SELF_UPLOAD_PHOTO?(Object(r["f"])(),Object(r["c"])("div",S,[Object(r["e"])("input",{onChange:t[2]||(t[2]=function(){return i.uploadImg&&i.uploadImg.apply(i,arguments)}),type:"file",class:"custom-file-input",id:"customFile"},null,32),B])):Object(r["d"])("",!0)])):Object(r["d"])("",!0)])}n("99af");var F={name:"user-card",props:{user:Object,displaySeeMoreBtn:Boolean,displayAddPhoto:Boolean},data:function(){return{photoPath:null,has_photo:!1}},methods:{changeUser:function(e){this.$emit("setUser",e)},uploadImg:function(e){var t=this;if(this.photoPath=e.target.files[0],this.photoPath){var n=new FormData;n.append("image",this.photoPath),M.a.post("".concat(this.$config.API_ENDPOINT,"/upload_photo/").concat(this.user.sAMAccountName),n).then((function(e){t.imagePath=e.data.path,t.$emit("hasPhoto",t.user.sAMAccountName)}))}}}};n("61d3");F.render=$;var L=F,H=Object(r["e"])("div",{id:"calendar"},null,-1);function G(e,t,n,c,o,i){return Object(r["f"])(),Object(r["c"])("div",null,[H])}var V=n("573d"),W=n("f665"),J=n.n(W),z=n("6f9a"),R=(n("52df"),n("7b50")),Y=n("3cdd"),q=n("a20c"),K=n("3e32"),Q=n("e44e"),X={name:"user-calendar",props:{user:Object},watch:{user:function(){this.setUpCalendar()}},data:function(){return{calendar:null,nextButton:null,previousButton:null}},mounted:function(){this.setUpCalendar(this.user)},methods:{setUpCalendar:function(){var e=document.getElementById("calendar");this.calendar=new V["a"](e,{locale:J.a,plugins:[Y["b"],K["a"],q["a"],R["a"],Q["a"]],initialView:"timeGridWeek",events:{url:"".concat(this.$config.API_ENDPOINT,"/caldav/").concat(this.user.mail)},slotMinTime:"06:00:00",slotMaxTime:"20:00:00",height:600,editable:!0,selectable:!0,headerToolbar:{left:"dayGridMonth,timeGridWeek,timeGridDay,listWeek",center:"title",right:"prev,next"},datesSet:this.dateChange,eventMouseEnter:this.handleMouseEnter,eventDidMount:this.handlEventDidMount}),this.calendar.render()},handleMouseEnter:function(e){console.log(e.event),console.log(e.event.extendedProps)},handlEventDidMount:function(e){var t="\n                <b> ".concat(e.event.title," </b> <br/>\n                <p> <b> Début </b> : ").concat(e.event.extendedProps.begin_str,"  </br>\n                    <b> Fin </b> : ").concat(e.event.extendedProps.end_str,"\n                </p>\n                <b> Participants </b>: ").concat(e.event.extendedProps.attendees,"\n            ");console.log(e.event),Object(z["a"])(e.el,{content:t,allowHTML:!0})}}};X.render=G;var Z=X,ee={name:"trombi-cal",props:{msg:String},components:{UserCard:L,UserCalendar:Z},mounted:function(){var e=this;M.a.get("".concat(this.$config.API_ENDPOINT,"/users_order_by_dep")).then((function(t){e.allUsers=t.data,e.filteredUsers=Object.assign(e.allUsers,{})}))},data:function(){return{departments:{},currentUser:null,allUsers:{},filteredUsers:{},searchPattern:null}},methods:{setCurrentUser:function(e){this.currentUser=e,this.filteredUsers=[]},setCurrDepartment:function(e){var t=this;this.currentUser=null,this.curDepartment=e,this.filteredUsers={},Object.keys(this.allUsers).map((function(n){e==n&&(t.filteredUsers[e]=t.allUsers[e])}))},refresh:function(){this.filteredUsers=this.allUsers,this.currentUser=null},changeHasPhotoProp:function(e){var t=this;Object.keys(this.allUsers).forEach((function(n){t.allUsers[n].forEach((function(t){e==t.sAMAccountName&&(t.has_photo=!0)}))}))},filterUsers:function(){var e=this;this.filteredUsers=Object.assign({},this.allUsers),0===this.searchPattern.length?this.filteredUsers=this.allUsers:Object.keys(this.filteredUsers).forEach((function(t){e.filteredUsers[t]=e.allUsers[t].filter((function(t){return-1!==t.displayName.toLowerCase().indexOf(e.searchPattern.toLowerCase())}))}))}}};n("c693");ee.render=C,ee.__scopeId="data-v-804c79dc";var te=ee,ne={name:"App",components:{TrombiCal:te}};n("8168");ne.render=c;var re=ne;M.a.get("".concat("","/config.json")).then((function(e){var t=Object(r["b"])(re);t.config.globalProperties.$config=e.data,t.mount("#app")}))},"61d3":function(e,t,n){"use strict";n("3ec0")},8168:function(e,t,n){"use strict";n("0937")},b5a1:function(e,t,n){var r={"./anne.bello.jpg":"ded1","./camille.monchicourt.jpg":"37b9"};function c(e){var t=o(e);return n(t)}function o(e){if(!n.o(r,e)){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}return r[e]}c.keys=function(){return Object.keys(r)},c.resolve=o,e.exports=c,c.id="b5a1"},c693:function(e,t,n){"use strict";n("3209")},cf05:function(e,t,n){e.exports=n.p+"img/logo.10acd893.png"},ded1:function(e,t,n){e.exports=n.p+"img/anne.bello.338966ca.jpg"},fc5b:function(e,t,n){e.exports=n.p+"img/no-photo.07b26464.jpg"}});
//# sourceMappingURL=app.f08210a5.js.map