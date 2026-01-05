const translations = {
  en: {
    title: "Environmental Monitoring — Public Demo",
    subtitle: "A synthetic, real-time monitoring and alerting demonstration",

    about_title: "About this project",
    about_text:
      "This demo showcases a complete monitoring stack built with Prometheus, Grafana, Alertmanager, and Gotify. All data is synthetic and generated in real time to simulate environmental conditions such as air quality, temperature, and CO₂ levels.",

    architecture_title: "Architecture overview",

    access_title: "Access & limitations",
    grafana_title: "Grafana",
    grafana_text: "Public access, read-only dashboards.",
    prometheus_title: "Prometheus",
    prometheus_text: "Public access for educational exploration.",
    gotify_title: "Gotify",
    gotify_text:
      "Login required. Demo users may delete messages; alerts will reappear automatically.",

    credentials_title: "Demo credentials",
    credentials_text:
      "Credentials are provided for demonstration purposes only. Please do not use them outside this demo.",

    footer:
      "© Demo project — All data is synthetic and for educational purposes only."
  },

  uz: {
    title: "Atrof-muhit monitoringi — Ochiq demo",
    subtitle: "Sun’iy ma’lumotlar asosidagi real vaqt monitoringi",

    about_title: "Loyiha haqida",
    about_text:
      "Ushbu demo Prometheus, Grafana, Alertmanager va Gotify asosida qurilgan monitoring tizimini namoyish etadi. Barcha ma’lumotlar sun’iy va real vaqt rejimida yaratiladi.",

    architecture_title: "Arxitektura",

    access_title: "Kirish va cheklovlar",
    grafana_title: "Grafana",
    grafana_text: "Ochiq kirish, faqat o‘qish rejimi.",
    prometheus_title: "Prometheus",
    prometheus_text: "Ta’limiy maqsadlar uchun ochiq.",
    gotify_title: "Gotify",
    gotify_text:
      "Kirish talab qilinadi. Demo foydalanuvchilar xabarlarni o‘chirishi mumkin.",

    credentials_title: "Demo ma’lumotlari",
    credentials_text:
      "Kirish ma’lumotlari faqat demo uchun berilgan.",

    footer:
      "© Demo loyiha — Barcha ma’lumotlar sun’iy."
  },

  ru: {
    title: "Мониторинг окружающей среды — Демо",
    subtitle: "Синтетическая демонстрация мониторинга в реальном времени",

    about_title: "О проекте",
    about_text:
      "Этот демо-проект показывает полный стек мониторинга на базе Prometheus, Grafana, Alertmanager и Gotify. Все данные синтетические.",

    architecture_title: "Архитектура",

    access_title: "Доступ и ограничения",
    grafana_title: "Grafana",
    grafana_text: "Публичный доступ, только просмотр.",
    prometheus_title: "Prometheus",
    prometheus_text: "Открыт для образовательных целей.",
    gotify_title: "Gotify",
    gotify_text:
      "Требуется вход. Демопользователи могут удалять сообщения.",

    credentials_title: "Демо-доступ",
    credentials_text:
      "Учетные данные предоставлены только для демонстрации.",

    footer:
      "© Демо-проект — Все данные синтетические."
  }
};

function setLang(lang) {
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (translations[lang][key]) {
      el.textContent = translations[lang][key];
    }
  });
}

// default language
setLang("uz");