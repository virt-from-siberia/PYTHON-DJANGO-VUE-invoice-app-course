/**
 * Утилита для обработки ошибок axios запросов
 * @param {Error} error - объект ошибки от axios
 * @param {Array} errorsArray - массив для добавления ошибок (обычно this.errors)
 * @returns {void}
 */
export function handleApiError(error, errorsArray) {
  if (error.response) {
    // Ошибка от сервера с ответом
    const errorData = error.response.data;

    // Обработка разных форматов ошибок
    if (typeof errorData === "object") {
      for (const property in errorData) {
        const errorValue = errorData[property];

        // Если значение - массив, объединяем его
        if (Array.isArray(errorValue)) {
          errorValue.forEach((err) => {
            errorsArray.push(`${property}: ${err}`);
          });
        } else {
          errorsArray.push(`${property}: ${errorValue}`);
        }
      }
    } else {
      errorsArray.push(errorData);
    }

    console.log("API Error Response:", JSON.stringify(errorData));
  } else if (error.message) {
    // Ошибка сети или другая ошибка
    errorsArray.push(`Network error: ${error.message}`);
    console.log("API Error Message:", JSON.stringify(error.message));
  } else {
    // Неизвестная ошибка
    errorsArray.push("An unexpected error occurred");
    console.log("API Error:", JSON.stringify(error));
  }
}
