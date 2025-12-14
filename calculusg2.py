function switchLang() {
    const url = new URL(window.location);
    const lang = url.searchParams.get('lang') === 'id' ? 'en' : 'id';
    url.searchParams.set('lang', lang);
    window.location = url;
}

// Simple i18n
const translations = {
    en: {
        title: 'Matrix Application',
        desc: 'Welcome to the Matrix Application. Choose a feature:',
        plot_link: 'Plot Function',
        opt_link: 'Optimization',
        func_label: 'Enter function (e.g., x**2 + 2*x):',
        plot_btn: 'Plot',
        deriv_label: 'Derivative:',
        back: 'Back',
        type_label: 'Problem Type:',
        params_label: 'Parameters (comma-separated):',
        solve_btn: 'Solve',
        result_label: 'Result:'
    },
    id: {
        title: 'Aplikasi Matriks',
        desc: 'Selamat datang di Aplikasi Matriks. Pilih fitur:',
        plot_link: 'Plot Fungsi',
        opt_link: 'Optimasi',
        func_label: 'Masukkan fungsi (contoh: x**2 + 2*x):',
        plot_btn: 'Plot',
        deriv_label: 'Turunan:',
        back: 'Kembali',
        type_label: 'Tipe Masalah:',
        params_label: 'Parameter (dipisah koma):',
        solve_btn: 'Selesaikan',
        result_label: 'Hasil:'
    }
};

document.addEventListener('DOMContentLoaded', function() {
    const lang = new URLSearchParams(window.location.search).get('lang') || 'en';
    const t = translations[lang];
    for (let key in t) {
        const el = document.getElementById(key);
        if (el) el.textContent = t[key];
    }
});
