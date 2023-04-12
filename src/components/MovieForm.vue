<template>
  <!-- your form template here -->
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    let csrf_token = ref("");

    function getCsrfToken() {
      fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          csrf_token.value = data.csrf_token;
        });
    }

    onMounted(() => {
      getCsrfToken();
    });

    function saveMovie() {
      let movieForm = document.getElementById('movieForm');
      let form_data = new FormData(uploadForm);
      fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
          'X-CSRFToken': csrf_token.value
        }
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          // display a success message
          console.log(data);
        })
        .catch(function (error) {
          console.log(error);
        });
    }

    return {
      csrf_token,
      saveMovie
    };
  }
}
</script>
