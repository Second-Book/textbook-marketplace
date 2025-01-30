<template>
  <div class="w-[1440px] h-[1024px] relative bg-white overflow-hidden">
    <div class="left-[150px] top-[17px] absolute">
      <img class="w-[100px] h-[100px] left-[1048px] top-0 absolute" :src="image.detail" alt="Textbook Image" />
    </div>
    <img class="w-3.5 h-[1024px] left-[1426px] top-0 absolute" src="https://via.placeholder.com/14x1024" />
    <div class="w-[480px] h-[47px] left-[150px] top-[136px] absolute text-black text-3xl font-bold font-['Inter']">{{ title }}</div>
    <div class="w-[578px] h-[195px] left-[720px] top-[148px] absolute">
      <div class="w-[472.06px] h-[108px] left-0 top-0 absolute text-black text-3xl font-bold font-['Inter']">{{ price }} rsd</div>
      <div class="w-[578px] h-[100px] left-0 top-[95px] absolute">
        <span class="text-black text-3xl font-bold font-['Inter']">{{ author }}<br/></span>
      </div>
    </div>
    <div class="w-[480px] h-[330px] left-[150px] top-[690px] absolute">
      <span class="text-black text-3xl font-medium font-['Inter']">Title:</span>
      <span class="text-black text-3xl font-normal font-['Inter']"> {{ title }}<br/><br/></span>
      <span class="text-black text-3xl font-medium font-['Inter']">Author:</span>
      <span class="text-black text-3xl font-normal font-['Inter']"> {{ author }}<br/><br/></span>
      <span class="text-black text-3xl font-medium font-['Inter']">Publisher:</span>
      <span class="text-black text-3xl font-normal font-['Inter']"> {{ publisher }}<br/><br/></span>
      <span class="text-black text-3xl font-medium font-['Inter']">Grade:</span>
      <span class="text-black text-3xl font-normal font-['Inter']"> {{ school_class }}<br/><br/></span>
      <span class="text-black text-3xl font-medium font-['Inter']">Condition:</span>
      <span class="text-black text-3xl font-normal font-['Inter']"> {{ condition }}<br/><br/><br/></span>
    </div>
    <div class="w-[596px] h-[330px] left-[720px] top-[690px] absolute">
      <span class="text-black text-3xl font-medium font-['Inter']">Description: <br></span>
      <span class="text-black text-3xl font-normal font-['Inter']">{{ description }}</span>
    </div>
    <div class="w-[120px] h-[23px] left-[510px] top-[633px] absolute text-[#525151] text-xl font-bold font-['Inter']">{{ time }}</div>
    <div class="w-[578px] h-[34px] left-[720px] top-[300px] absolute">
      <span class="text-black text-3xl font-medium font-['Inter'] underline">Location:</span>
      <span class="text-black text-3xl font-normal font-['Inter'] underline">{{ location }}</span>
    </div>
    <div class="w-[578px] h-[77px] left-[720px] top-[358px] absolute">
      <span class="text-black text-3xl font-medium font-['Inter']">Contacts:</span>
      <div class="flex flex-col gap-4">
        <template v-if="whatsapp_contact">
          <div class="flex items-center">
            <img class="h-6 w-6" :src="whatsappUrl" />
            <span class="text-3xl mr-2">{{ whatsapp_contact }}</span>
          </div>
        </template>
        <template v-if="telegram_contact">
          <div class="flex items-center">
            <img class="h-6 w-6" :src="telefonUrl" />
            <span class="text-3xl mr-2">{{ telegram_contact }}</span>
          </div>
        </template>
        <template v-if="viber_contact">
          <div class="flex items-center">
            <img class="h-6 w-6" :src="viberUrl" />
            <span class="text-3xl mr-2">{{ viber_contact }}</span>
          </div>
        </template>
        <template v-if="phone_contact">
          <div class="flex items-center">
            <img class="h-6 w-6" src="https://cdn-icons-png.flaticon.com/512/2983/2983864.png" />
            <span class="text-3xl mr-2">{{ phone_contact }}</span>
          </div>
        </template>
      </div>
    </div>
    <div class="w-[483.33px] h-[420px] left-[150px] top-[213px] absolute">
      <div class="w-[480px] h-[420px] left-0 top-0 absolute bg-[#d9d9d9] flex items-center justify-center">
        <img class="max-w-full max-h-full" :src="image.detail" alt="Textbook Image" />
      </div>
    </div>
    <div class="w-[120px] h-[24.23px] left-[1050px] top-[43px] absolute">
      <div class="w-[120px] h-[24.23px] left-0 top-0 absolute rounded-[10px]"></div>
    </div>
  </div>
</template>


<script>
import textbookService from '../services/TextbookService.js';


export default {
  name: 'Textbook',
  components: {
  },
  data() {
    return {
      key: null,
      title: null,
      author: null,
      publisher: null,
      price: null,
      school_class: null,
      condition: null,
      description: null,
      seller: null,
      location: null,
      contacts: null,
      image: null,
      whatsappUrl: 'https://cdn.builder.io/api/v1/image/assets/f4c1588a1e044eaca829846f2a5403d3/b18ff27f2b78f4e9aa6c8a35213e6b106a72321e60a304ddc154e27d7b7c16b8?apiKey=f4c1588a1e044eaca829846f2a5403d3&',
      telefonUrl: 'https://cdn.builder.io/api/v1/image/assets/f4c1588a1e044eaca829846f2a5403d3/4b444aee593aca3ef65b8c5754d7df1cf22b4aef792e21d8d86c495b32ce79a2?apiKey=f4c1588a1e044eaca829846f2a5403d3&',
      viberUrl: 'https://cdn.builder.io/api/v1/image/assets/f4c1588a1e044eaca829846f2a5403d3/cbbc97949bf833e15266f0be56b1ee56fa57a024e8c6d69e2358458c4cae81b2?apiKey=f4c1588a1e044eaca829846f2a5403d3&',
    }
    },
  created() {
    this.id = this.$route.params.id;
    textbookService.getTextbook(this.id)
      .then(response => {
        this.title = response.data.title;
        this.author = response.data.author;
        this.publisher = response.data.publisher;
        this.school_class = response.data.school_class; 
        this.condition = response.data.condition;
        this.description = response.data.description;
        this.price = response.data.price;
        this.seller = response.data.seller;
        this.location = response.data.location;
        this.whatsapp_contact = response.data.whatsapp_contact;
        this.phone_contact = response.data.phone_contact;
        this.viber_contact = response.data.viber_contact;
        this.telegram_contact = response.data.telegram_contact;
        this.image = {
          detail: `http://localhost:8000${response.data.image.detail}`,
        };
      })
      .catch(error => {
        console.error('Error fetching textbook:', error);
      });
  }
};
</script>

<style>
.flex {
  display: flex;
  flex-wrap: wrap;
}

.flex-wrap {
  flex-wrap: wrap;
}

.gap-4 {
  gap: 1rem;
}

.icon {
  height: 1.2em;
  vertical-align: middle;
  margin-right: 0.5rem;
}

.ml-2 {
  margin-left: 0.5rem;
}
.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}
</style>

