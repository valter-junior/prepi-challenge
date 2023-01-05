<template>
  <div>
    <div class="img">
      <v-row justify="center" align="center">
        <img src="~/assets/images/prepi.png" />
      </v-row>
    </div>
    <v-row justify="center" align="center">
      <div class="text-center align-center justify-center">
        <v-btn to="register" class="mt-4" color="grey darken-1"
          >Registrar Produto</v-btn
        >
      </div>
      &nbsp;&nbsp;&nbsp;
      <div class="text-center align-center justify-center">
        <v-btn to="register" class="mt-4" color="grey darken-1"
          >Ordem de Venda</v-btn
        >
      </div>
    </v-row>

    <v-navigation-drawer
      absolute
      v-model="drawer"
      :mini-variant.sync="mini"
      permanent
      light
    >
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>John Leider</v-list-item-title>

        <v-btn icon @click.stop="mini = !mini">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item v-for="item in items" :key="item.title" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      items: [
        { title: "Home", icon: "mdi-home-city" },
        { title: "My Account", icon: "mdi-account" },
        { title: "Users", icon: "mdi-account-group-outline" },
      ],
      mini: true,
    };
  },
};
</script>

<style scoped>
.body {
  padding: 100px;
}
.img {
  padding: 24px;
  height: 12%;
  align-content: center;
  justify-content: center;
}
</style>