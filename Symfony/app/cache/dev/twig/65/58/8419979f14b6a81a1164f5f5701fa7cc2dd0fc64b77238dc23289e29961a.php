<?php

/* TutoTestBundle:Default:index.html.twig */
class __TwigTemplate_65588419979f14b6a81a1164f5f5701fa7cc2dd0fc64b77238dc23289e29961a extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "the name of the film is ";
        echo twig_escape_filter($this->env, (isset($context["film"]) ? $context["film"] : $this->getContext($context, "film")), "html", null, true);
        echo "! <br>
the realisator of the film is ";
        // line 2
        echo twig_escape_filter($this->env, (isset($context["realisator"]) ? $context["realisator"] : $this->getContext($context, "realisator")), "html", null, true);
        echo "!
";
    }

    public function getTemplateName()
    {
        return "TutoTestBundle:Default:index.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  24 => 2,  19 => 1,);
    }
}
