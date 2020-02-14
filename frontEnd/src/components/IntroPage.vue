<template>
  <div class="hello">
    <el-row>
      <div class="item-container">
        <div class="top-tips"><p>{{tips[0]}}</p></div>
        <el-row style="">
          <el-col :span="12">
            <el-upload
            class="upload-img"
            :action="uploadUrl"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :before-upload="beforeAvatarUpload"
            :limit="1"
            :on-exceed="handleExceed"
            :on-success="handleAvatarSuccess"
            :file-list="fileList">
            <el-button plain type="info" style="font-size: 18px;">Click to upload</el-button>
            <div slot="tip" class="el-upload__tip" style="font-size: 18px;"> Only can upload a <b>Single</b> jpg/png file</div>
          </el-upload>
          </el-col>
        </el-row>
      </div>
    </el-row>
    <el-row>
      <div style="height: 20px;"></div>
    </el-row>
    <div class="item-container">
      <div class="top-tips"><p>{{tips[1]}}</p></div>
      <el-row :gutter="10">
        <el-col :span="8">
          <div class="img-container">
            <el-card :body-style="{ padding: '0px' }">
              <div v-loading="loading_A">
                <img :src="imgList[0].url" alt="" class="show-img">
              </div>
              <div style="padding: 14px;">
                <span>Original Image</span>
                <p>{{introImg[0]}}<br></p>
              </div>
            </el-card>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="img-container">
            <el-card :body-style="{ padding: '0px' }">
              <div v-loading="loading_A">
                <img :src="imgList[1].url" alt="" class="show-img">
              </div>
              <div style="padding: 14px;">
                <span>Outline</span>
                <p>{{introImg[1]}}</p>
              </div>
            </el-card>
          </div>
        </el-col>
        <!-- <el-col :span="1">
          <img style="width: 80px; margin-top: 80px; margin-left: 10px;" src="@/assets/pointer2.png" alt="">
        </el-col> -->
        <el-col :span="8">
          <div class="img-container">
            <el-card :body-style="{ padding: '0px' }">
              <div v-loading="loading_A">
                <img :src="imgList[2].url" alt="" class="show-img">
              </div>
              <div style="padding: 14px;">
                <span>Original Image + Outline</span>
                <p>{{introImg[2]}}</p>
              </div>
            </el-card>
          </div>
        </el-col>
      </el-row>
    </div>
    <el-row>
      <div style="height: 15px;"></div>
    </el-row>
    <div class="item-container" style="padding: 55px 0 0 0">
      <div class="top-tips"><p>{{tips[2]}}</p></div>
      <el-row>
        <div class="img-container">
          <el-card :body-style="{ padding: '0px' }">
            <div class="result">
              <h3>Recongnition Result: </h3>
              <div class="result-percentage">
                <p>Bulk Carrier</p>
                <el-progress :stroke-width="14" :color="customColors" :percentage="bulk"></el-progress>
              </div>
              <div class="result-percentage">
                <p>Container ship</p>
                <el-progress :stroke-width="14" :color="customColors" :percentage="container"></el-progress>
              </div>
              <div class="result-percentage">
                <p>cruise ship</p>
                <el-progress :stroke-width="14" :color="customColors" :percentage="cruise"></el-progress>
              </div>
            </div>
            <!-- <img v-bind:src="imgList[0].url" class="show-img"> -->
            <div v-loading="loading_B">
              <img :src="imgList[0].url" alt="" class="show-result-img">
            </div>
            <div style="padding: 14px;">
              <span>This boat is <span style="color: red;">{{result[0]}}</span></span>
            </div>
          </el-card>
        </div>
      </el-row>
    </div>
    <el-row>
      <div style="height: 20px;"></div>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'IntroPage',
  data () {
    return {
      fileList: [],
      isJPGPNG: false,
      imgList: [
        {
          name: 'original',
          url: 'http://localhost:8000/backend/EXAMPLE.jpg'
        },
        {
          name: 'outline',
          url: 'http://localhost:8000/backend/d_EXAMPLE.jpg'
        },
        {
          name: 'original_outline',
          url: 'http://localhost:8000/backend/o_EXAMPLE.jpg'
        }
      ],
      result: ['Bulk Carrier', 'Kind Two', 'Kind Three'],
      tips: ['First step: upload a boat imge', 'Second step: prepare the input image', 'Final step: recognize the kind of this boat'],
      introImg: ['This is the original imge.', 'In this step, we calculate the Outline by grayscale.', 'Finally, the orignal image and ouline image are combined to get the final input image.'],
      percentage: [],
      bulk: 0,
      container: 0,
      cruise: 0,
      customColors: [
        {color: '#f56c6c', percentage: 20},
        {color: '#e6a23c', percentage: 40},
        {color: '#e6a23c', percentage: 60},
        {color: '#5cb87a', percentage: 80},
        {color: '#5cb87a', percentage: 100}
      ],
      uploadUrl: 'http://localhost:8000/backend/',
      loading_A: false,
      loading_B: false
    }
  },
  methods: {
    url (index) {
      return require(`@/assets/images/${this.imgList[index].url}`)
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    beforeAvatarUpload (file) {
      console.log(file.type)
      this.isJPGPNG = false
      if (file.type === 'image/jpeg' || file.type === 'image/png') {
        this.isJPGPNG = true
        this.loading_A = true
        this.loading_B = true
      }
      if (!this.isJPGPNG) {
        this.$message.warning(`Only JPG / PNG files are allowed`)
      }
    },
    handleExceed (files, fileList) {
      this.$message.warning(`The number of files is currently limited to one, ${files.length} files are selected this time, ${files.length + fileList.length} files are selected in total. Please delete ${fileList[0].name} first.`)
    },
    beforeRemove (file, fileList) {
      return this.$confirm(`Delect ${file.name}？`)
    },
    format (percentage) {
      return percentage === 100 ? '满' : `${percentage}%`
    },
    // 自定义上传图片方法（未用）
    uploadImage (content) {
      var form = new FormData()
      var t = this.$axios
      form.append('file', content.file)
      this.$axios.post(content.action, form)
        .then(res => {
          console.log('post img --> res')
          console.log(res)
          console.log(res.data['original'])
          this.imgList[0].url = 'http://localhost:8000/backend/' + res.data['original']
          this.imgList[1].url = 'http://localhost:8000/backend/' + res.data['outline']
          this.imgList[2].url = 'http://localhost:8000/backend/' + res.data['original_outline']
          t.get('predict/')
            .then(res => {
              console.log('predict --> res')
              console.log(res)
            })
            .catch(error => {
              console.log('predict --> error')
              console.log(error)
            })
        })
        .catch(error => {
          console.log('post img --> error')
          console.log(error)
        })
    },
    // 成功上传钩子函数
    handleAvatarSuccess (response) {
      console.log(response)
      this.imgList[0].url = 'http://localhost:8000/backend/' + response['original']
      this.imgList[1].url = 'http://localhost:8000/backend/' + response['outline']
      this.imgList[2].url = 'http://localhost:8000/backend/' + response['original_outline']
      this.loading_A = false
      this.$axios.get('/backend/predict/')
        .then(res => {
          console.log('predict --> res')
          console.log(res)
          this.bulk = res.data['bulk']
          this.container = res.data['container']
          this.cruise = res.data['cruise']
          this.loading_B = false
        })
        .catch(error => {
          console.log('predict --> error')
          console.log(error)
        })
    },
    predict () {
      console.log(this.percentage[0])
      this.bulk = 34
      this.container = 35
      this.cruise = 97
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import './../assets/css/IntroPage.css';
</style>
