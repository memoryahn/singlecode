<template>
<div style="padding:1em" align="center">
<div style="width:700px">
    <div class="flex">
      <div class="title" style="flex:2">이름</div>
      <div class="title" style="flex:1">코드</div>
      <div class="title" style="flex:2">BITHUMB</div>
      <div class="title" style="flex:2">GOPAX</div>
      <div class="title" style="flex:1">BIT-GO</div>
      <div class="title" style="flex:2">UPBIT</div>
      <div class="title" style="flex:1">BIT-UP</div>
    </div>
    <div v-for="code in data" class="flex" :key="code.code">
      <div class="data" style="flex:2" align="left">{{ code.name }}</div>
      <div class="data" style="flex:1">{{ code.code }}</div>
      <div class="data" style="flex:2" align="right">{{ comma(code.bithumb) }}</div>
      
      <div v-if="code.bg >= 0 " class="data red" style="flex:2" align="right">{{ comma(code.gopax) }}</div>
      <div v-if="code.bg >= 0 " class="data red" style="flex:1" align="right">{{ code.bg }}%</div>
      <div v-if="code.bu >= 0 " class="data red" style="flex:2" align="right">{{ comma(code.upbit) }}</div>
      <div v-if="code.bu >= 0 " class="data red" style="flex:1" align="right">{{ code.bu }}%</div>
      
      <div v-if="code.bg < 0 " class="data blue" style="flex:2" align="right">{{ comma(code.gopax) }}</div>
      <div v-if="code.bg < 0 " class="data blue" style="flex:1" align="right">{{ code.bg }}%</div>
      <div v-if="code.bu < 0 " class="data blue" style="flex:2" align="right">{{ comma(code.upbit) }}</div>
      <div v-if="code.bu < 0 " class="data blue" style="flex:1" align="right">{{ code.bu }}%</div>
    </div>
</div>
</div>
</template>
<script>

import axios from 'axios'
import Vue from 'vue'
var tim
export default {
  data() {
    return {
      data:{},
    }
  },
  methods: {
      comma(nStr){
      nStr += '';
      var x = nStr.split('.');
      var x1 = x[0];
      var x2 = x.length > 1 ? '.' + x[1] : '';
      var rgx = /(\d+)(\d{3})/;
      while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
      }
      return x1 + x2;
    },
    getdata(){
        axios.get('http://127.0.0.1:5000/')
    .then(response=>{
      console.log('connect')
      this.data=response.data
      for (let i in this.data){
        Vue.set(this.data[i],'bg',(((this.data[i].gopax-this.data[i].bithumb)/this.data[i].bithumb)*100).toFixed(2))
        Vue.set(this.data[i],'bu',(((this.data[i].upbit-this.data[i].bithumb)/this.data[i].bithumb)*100).toFixed(2))
      }
    })
    .catch(e=>{
      console.log(e)
    })
    }
  },
  created() {
      this.getdata()
      tim=setInterval(function() {this.getdata()}.bind(this),5000)
  },
  destroyed() {
      clearInterval(tim)
  }
}
</script>
<style>
.flex {
  display: flex
}
.info {
  border: 1px solid lightgray;
  color: green;
  padding: 5px
}
.title {
  border: 1px solid lightgray;
  color: brown;
  padding: 5px
}
.data {
  border: 1px solid lightgray;
  font-size:12px;
  padding: 5px
}
.red {
    color:red;
}
.blue {
    color:blue;
}
#dd:nth-child(odd){
  background: #eee;
}
</style>
