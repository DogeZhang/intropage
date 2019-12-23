<template>
  <div class="hello">
    <el-row>
      <div style="height: 20px;"></div>
    </el-row>
    <el-row>
      <el-col :span="8">
        <el-upload
        class="upload-img"
        action="https://localhost:8080/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        :before-upload="beforeAvatarUpload"
        multiple
        :limit="1"
        :on-exceed="handleExceed"
        :file-list="fileList">
        <el-button size="small" type="primary" style="font-size: 18px;">Click to upload</el-button>
        <div slot="tip" class="el-upload__tip" style="font-size: 18px; color: rgb(4, 22, 77);"> Only can upload <b>Single</b> jpg/png file</div>
      </el-upload>
      </el-col>
    </el-row>
    <el-row>
      <div style="height: 15px;"></div>
    </el-row>
    <el-row>
      <el-col :span="8">
        <div class="img-container">
          <el-card :body-style="{ padding: '0px' }">
            <!-- <img v-bind:src="imgList[0].url" class="show-img"> -->
            <img :src="url(0)" alt="" class="show-img">
            <div style="padding: 14px;">
              <span>Original Drawing</span>
            </div>
          </el-card>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="img-container">
          <el-card :body-style="{ padding: '0px' }">
            <img src="@/assets/outline.jpg" class="show-img">
            <div style="padding: 14px;">
              <span>Outline</span>
            </div>
          </el-card>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="img-container">
          <el-card :body-style="{ padding: '0px' }">
            <img src="../assets/original_outline.jpg" class="show-img">
            <div style="padding: 14px;">
              <span>OD + Outline</span>
            </div>
          </el-card>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <div style="height: 15px;"></div>
    </el-row>
    <el-row>
      <h2>Recongnition Result: </h2>
      <div class="img-container">
        <el-card :body-style="{ padding: '0px' }">
          <!-- <img v-bind:src="imgList[0].url" class="show-img"> -->
          <img :src="url(0)" alt="" class="show-img">
          <div style="padding: 14px;">
            <span>This boat is <span style="color: red;">{{result[0]}}</span></span>
          </div>
        </el-card>
      </div>
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
          url: 'original.jpg'
        },
        {
          name: 'outline',
          url: 'outline.jpg'
        },
        {
          name: 'original_outline',
          url: 'original_outline.jpg'
        }
      ],
      result: ['Bulk Carrier', 'Kind Two', 'Kind Three']
    }
  },
  methods: {
    url (index) {
      return require(`@/assets/${this.imgList[0].url}`)
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
      }
      if (!this.isJPGPNG) {
        this.$message.warning(`Only JPG / PNG files are allowed`)
      }
    },
    handleExceed (files, fileList) {
      this.$message.warning(`The number of files is currently limited to one, ${files.length} files are selected this time, ${files.length + fileList.length} files are selected in total.`)
    },
    beforeRemove (file, fileList) {
      return this.$confirm(`Delect ${file.name}？`)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}
.hello{
  margin: 0 auto;
  max-width: 1200px;
}
.img-container{
  font-size: 24px;
  width: 380px;
}
.show-img{
  width: 380px;
}
</style>
