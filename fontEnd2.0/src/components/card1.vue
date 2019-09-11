<template>
    <div>
        <Card :bordered=false v-for="item in itemList" :key="item.title" class="card">
            <p slot="title">
                <Icon type="ios-film-outline"></Icon>
                {{item.title}}
            </p>
            <!-- <a href="#" slot="extra" @click.prevent="changeLimit">
                <Icon type="ios-loop-strong"></Icon>
                {{item.url}}
            </a> -->
            <wordinpic :get-data= item.title :get-img= item.img :get-txt= item.txt @childFn="changePage"></wordinpic>
            <!-- <ul>
                <li v-for="item in randomMovieList">
                    <a :href="item.url" target="_blank">{{ item.name }}</a>
                    <span>
                        <Icon type="ios-star" v-for="n in 4" :key="n"></Icon><Icon type="ios-star" v-if="item.rate >= 9.5"></Icon><Icon type="ios-star-half" v-else></Icon>
                        {{ item.rate }}
                    </span>
                </li>
            </ul> -->
            <ul>
                <div class="sj">
                <Icon type="ios-calendar"></Icon>
                {{item.lrrq}}
                </div>
            </ul>
        </Card>
        <Page show-elevator :total="dataCount" :page-size="pageSize" :current="pageCurrent"
            @on-change="change" @on-page-size-change="_nowPageSize" show-total show-sizer show-elevator></Page>
    </div>
</template>

<script>
import wordinpic from '@/components/wordinpic'
import { search_geciList } from '@/api/api.js'
export default {
    components: {
        wordinpic
    },
    methods:{
        changePage(pagemsg){
            this.$emit('changePage',pagemsg);
            console.log(this.pages)
        },
        change(index){
            console.log(index);
            this.pageCurrent = index;
            this._getData();
        },
        _nowPageSize(index) {
            console.log(index);
            this.pageSize = index;
            this._getData();
        },
        _getData(){
            let postData = {
                'pageCurrent': this.pageCurrent,
                'pageSize' : this.pageSize
            }
            search_geciList(postData).then(res => {
                console.log(res.data.geciList);
                this.dataCount = res.data.dataCount;
                this.itemList = res.data.geciList;
            })
        }
    },
    data() {
        return {
            itemList: [],
            pages: '',
            dataCount: 0,
            pageSize: 10,
            pageCurrent: 1
        }
    },
    mounted() {
        search_geciList().then(res => {
            console.log(res.data.geciList);
            this.dataCount = res.data.dataCount;
            this.itemList = res.data.geciList;
        })
    }
}
</script>

<style scoped>
    .card{
        margin-bottom: 10px;
    }
    .sj{
        font-size: 15px;
    }
</style>